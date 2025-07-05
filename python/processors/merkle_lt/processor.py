from time import perf_counter
import json
import logging
from typing import List

from aptos_protos.aptos.transaction.v1 import transaction_pb2
from utils import general_utils
from utils.transactions_processor import ProcessingResult, TransactionsProcessor
from utils.session import Session
from utils.processor_name import ProcessorName
from utils.models.schema_names import MERKLE_SCHEMA_NAME  


from processors.merkle_lt.models import (
    # delegate_account events
    MerkleDelegateAccountDelegateAccountVaultEvent,
    MerkleDelegateAccountRegisterEvent,
    MerkleDelegateAccountClaimEvent,
    MerkleDelegateAccountRebateEvent,
    # fee_distributor events
    MerkleFeeDistributorDepositFeeEvent,
    # gear events
    MerkleGearEquipEvent,
    MerkleGearGearEffectEvent,
    MerkleGearUnequipEvent,
    MerkleGearSalvageEvent,
    MerkleGearRepairEvent,
    MerkleGearMintEvent,
    MerkleGearForgeEvent,
    # house_lp events
    MerkleHouseLpRedeemEvent,
    MerkleHouseLpFeeEvent,
    MerkleHouseLpDepositEvent,
    MerkleHouseLpDepositEvent,
    # liquidity_auction events
    MerkleLiquidityAuctionWithdrawAssetEvent,
    MerkleLiquidityAuctionDepositPreMklEvent,
    MerkleLiquidityAuctionDepositAssetEvent,
    # lootbox events
    MerkleLootboxLootBoxOpenEvent,
    MerkleLootboxLootBoxEvent,
    # lootbox_v2 events
    MerkleLootboxV2LootBoxOpenEvent,
    MerkleLootboxV2FtuLootBoxEvent,
    MerkleLootboxV2LootBoxEvent,
    # mkl_token events
    MerkleMklTokenDelegateAccountVaultEvent,
    # pMKL events
    MerklePmklClaimEvent,
    MerklePmklMintEvent,
    # pre_tge_reward events
    MerklePreTgeRewardClaimEvent,
    # profile events
    MerkleProfileIncreaseBoostEvent,
    MerkleProfileIncreaseXPEvent,
    MerkleProfileSoftResetEvent,
    # referral events
    MerklereferralProtocolRevenueEvent,
    # shard_token events
    MerkleshardsTokenBurnEvent,
    MerkleshardsTokenMintEvent,
    # staking events
    MerklestakingUnlockEvent,
    MerklestakingLockEvent,
    # trading events
    MerkleTradingUpdateTPSLEvent,
    MerkleTradingPlaceOrderEvent,
    MerkleTradingPositionEvent,
    MerkleTradingCancelOrderEvent,
    # username events
    MerkleUsernameUsernameRegisterEvent,
    MerkleUsernameTicketIssueEvent,
    MerkleUsernameUsernameDeleteEvent,
    MerkleHouseLpRedeemCancelEvent
)

# List of module names (the second segment of the event type string) that we are tracking.
MODULE_ADDRESS = general_utils.standardize_address(
    "0x5ae6789dd2fec1a9ec9cccfb3acaf12e93d432f0a3a42c92fe1a9d490b7bbc06"
)

class MerkleProcessor(TransactionsProcessor):
    def name(self) -> str:
        return ProcessorName.MERKLE_PROCESSOR.value

    def schema(self) -> str:
        return MERKLE_SCHEMA_NAME

    def process_transactions(
        self,
        transactions: list[transaction_pb2.Transaction],
        start_version: int,
        end_version: int,
    ) -> ProcessingResult:
        event_db_objs = []
        start_time = perf_counter()

        for transaction in transactions:
            # Only process user transactions
            if transaction.type != transaction_pb2.Transaction.TRANSACTION_TYPE_USER:
                continue

            transaction_version = transaction.version
            transaction_timestamp = general_utils.parse_pb_timestamp(transaction.timestamp)
            user_transaction = transaction.user
            sender_address = general_utils.standardize_address(user_transaction.request.sender)

            # Process events in the transaction
            for event_index, event in enumerate(user_transaction.events):
                # Check if event belongs to one of our tracked modules
                if not MerkleProcessor.included_event_type(event.type_str):
                    continue

                logging.info(
                    "[Parser] Processing transaction",
                    extra={
                        "processor_name": self.name(),
                        "transaction_version": str(transaction_version),
                        "service_type": "processor",
                    },
                )
                try:
                    # Log raw address and event data for debugging
                    raw_address = event.key.account_address
                    logging.debug(f"[DEBUG] Raw address: {raw_address}")
                    account_address_std = general_utils.standardize_address(raw_address)
                    logging.debug(f"[DEBUG] Standardized address: {account_address_std}")
                    event_data = json.loads(event.data)
                    logging.debug(f"[DEBUG] Event data: {event_data}")
                    logging.debug(f"[DEBUG] Event type: {event.type_str}")
                except Exception as e:
                    logging.error(f"[DEBUG] Error processing event data: {str(e)}")
                    continue

                # Common event fields
                creation_number = event.key.creation_number
                sequence_number = event.sequence_number
                account_address = event.key.account_address  # original address from event key
                identifier = int(f"{transaction_version}{event_index}")
                event_type_full = event.type_str
                parts = event_type_full.split("::")
                if len(parts) < 3:
                    continue
                # parts[0] is the module address, parts[1] is module name, parts[2] is event type
                module_name = parts[-2]
                event_type = parts[-1]

                event_obj = None
                data = event_data  # alias

                # --- delegate_account module ---
                if module_name == "delegate_account":
                    if event_type == "DelegateAccountVaultEvent":
                        event_obj = MerkleDelegateAccountDelegateAccountVaultEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            amount=int(data["amount"]),
                            event_type=int(data["event_type"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "RegisterEvent":
                        event_obj = MerkleDelegateAccountRegisterEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            referrer=data["referrer"],
                            referee=data["referee"],
                            registered_at=int(data["registered_at"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "ClaimEvent":
                        event_obj = MerkleDelegateAccountClaimEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            amount=int(data["amount"]),
                            epoch=int(data["epoch"]),
                            extras=str(data["extras"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "RebateEvent":
                        event_obj = MerkleDelegateAccountRebateEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            referrer=data["referrer"],
                            referee=data["referee"],
                            rebate=int(data["rebate"]),
                            rebate_rate=int(data["rebate_rate"]),
                            epoch=int(data["epoch"]),
                            extras=str(data["extras"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- fee_distributor module ---
                elif module_name == "fee_distributor":
                    if event_type == "DepositFeeEvent":
                        event_obj = MerkleFeeDistributorDepositFeeEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            lp_amount=int(data["lp_amount"]),
                            stake_amount=int(data["stake_amount"]),
                            dev_amount=int(data["dev_amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- gear module ---
                elif module_name == "gear":
                    if event_type == "EquipEvent":
                        event_obj = MerkleGearEquipEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            gear_address=data["gear_address"],
                            user=data["user"],
                            durability=int(data["durability"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "GearEffectEvent":
                        event_obj = MerkleGearGearEffectEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            gear_address=data["gear_address"],
                            # For nested structures such as pair_type, store as JSON or a stringified dict.
                            #pair_type=json.dumps(data["pair_type"]),
                            pair_type_account_address = data["pair_type"]["account_address"],
                            pair_type_module_name = data["pair_type"]["module_name"],
                            pair_type_struct_name = data["pair_type"]["struct_name"],
                            
                            user=data["user"],
                            effect=int(data["effect"]),
                            gear_type=int(data["gear_type"]),
                            gear_code=int(data["gear_code"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "UnequipEvent":
                        event_obj = MerkleGearUnequipEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            gear_address=data["gear_address"],
                            user=data["user"],
                            durability=int(data["durability"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "SalvageEvent":
                        event_obj = MerkleGearSalvageEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            gear_address=data["gear_address"],
                            shard_amount=int(data["shard_amount"]),
                            user=data["user"],
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "RepairEvent":
                        event_obj = MerkleGearRepairEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            gear_address=data["gear_address"],
                            shard_amount=int(data["shard_amount"]),
                            user=data["user"],
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "MintEvent":
                        event_obj = MerkleGearMintEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            gear_address=data["gear_address"],
                            season=int(data["season"]),
                            user=data["user"],
                            name=data["name"],
                            uri=data["uri"],
                            gear_type=int(data["gear_type"]),
                            gear_code=int(data["gear_code"]),
                            tier=int(data["tier"]),
                            primary_effect=int(data["primary_effect"]),
                            # gear_affixes is a vector – store as JSON string
                            gear_affixes=str(data["gear_affixes"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "ForgeEvent":
                        event_obj = MerkleGearForgeEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            gear1_uid=int(data["gear1_uid"]),
                            gear1_address=data["gear1_address"],
                            gear2_uid=int(data["gear2_uid"]),
                            gear2_address=data["gear2_address"],
                            required_shard=int(data["required_shard"]),
                            gear_tier=int(data["gear_tier"]),
                            result_tier=int(data["result_tier"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- house_lp module ---
                elif module_name == "house_lp":
                    if event_type == "RedeemEvent":
                        event_obj = MerkleHouseLpRedeemEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            #asset_type=json.dumps(data["asset_type"]),
                            asset_type_account_address = data["asset_type"]["account_address"],
                            asset_type_module_name = data["asset_type"]["module_name"],
                            asset_type_struct_name = data["asset_type"]["struct_name"],
                            
                            burn_amount=int(data["burn_amount"]),
                            withdraw_amount=int(data["withdraw_amount"]),
                            redeem_amount_left=int(data["redeem_amount_left"]),
                            withdraw_fee=int(data["withdraw_fee"]),
                            started_at_sec=int(data["started_at_sec"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "FeeEvent":
                        event_obj = MerkleHouseLpFeeEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            fee_type=int(data["fee_type"]),
                            #asset_type=json.dumps(data["asset_type"]),
                            asset_type_account_address = data["asset_type"]["account_address"],
                            asset_type_module_name = data["asset_type"]["module_name"],
                            asset_type_struct_name = data["asset_type"]["struct_name"],
                            
                            amount=int(data["amount"]),
                            amount_sign=bool(data["amount_sign"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "DepositEvent":
                        event_obj = MerkleHouseLpDepositEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            #asset_type=json.dumps(data["asset_type"]),
                            asset_type_account_address = data["asset_type"]["account_address"],
                            asset_type_module_name = data["asset_type"]["module_name"],
                            asset_type_struct_name = data["asset_type"]["struct_name"],
                            
                            user=data["user"],
                            deposit_amount=int(data["deposit_amount"]),
                            mint_amount=int(data["mint_amount"]),
                            deposit_fee=int(data["deposit_fee"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "RedeemCancelEvent":
                        event_obj = MerkleHouseLpRedeemCancelEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            return_amount=int(data["return_amount"]),
                            initial_amount=int(data["initial_amount"]),
                            started_at_sec=int(data["started_at_sec"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- liquidity_auction module ---
                elif module_name == "liquidity_auction":
                    if event_type == "WithdrawAssetEvent":
                        event_obj = MerkleLiquidityAuctionWithdrawAssetEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            #asset_type=json.dumps(data["asset_type"]),
                            asset_type_account_address = data["asset_type"]["account_address"],
                            asset_type_module_name = data["asset_type"]["module_name"],
                            asset_type_struct_name = data["asset_type"]["struct_name"],
                            
                            asset_withdraw_amount=int(data["asset_withdraw_amount"]),
                            asset_total_amount=int(data["asset_total_amount"]),
                            phase1_asset_deposit_amount=int(data["phase1_asset_deposit_amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "DepositPreMklEvent":
                        event_obj = MerkleLiquidityAuctionDepositPreMklEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            pre_mkl_deposit_amount=int(data["pre_mkl_deposit_amount"]),
                            total_pre_mkl_deposit_amount=int(data["total_pre_mkl_deposit_amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "DepositAssetEvent":
                        event_obj = MerkleLiquidityAuctionDepositAssetEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            #asset_type=json.dumps(data["asset_type"]),
                            asset_type_account_address = data["asset_type"]["account_address"],
                            asset_type_module_name = data["asset_type"]["module_name"],
                            asset_type_struct_name = data["asset_type"]["struct_name"],
                            
                            asset_deposit_amount=int(data["asset_deposit_amount"]),
                            phase1_asset_deposit_amount=int(data["phase1_asset_deposit_amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- lootbox module ---
                elif module_name == "lootbox":
                    if event_type == "LootBoxOpenEvent":
                        event_obj = MerkleLootboxLootBoxOpenEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            tier=int(data["tier"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "LootBoxEvent":
                        event_obj = MerkleLootboxLootBoxEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            # Assuming lootbox is a vector of u64 values – store as JSON
                            lootbox=str(data["lootbox"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- lootbox_v2 module ---
                elif module_name == "lootbox_v2":
                    if event_type == "LootBoxOpenEvent":
                        event_obj = MerkleLootboxV2LootBoxOpenEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            season=int(data["season"]),
                            user=data["user"],
                            tier=int(data["tier"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "FtuLootBoxEvent":
                        event_obj = MerkleLootboxV2FtuLootBoxEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            reward_tier=int(data["reward_tier"]),
                            referrer=data["referrer"],
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "LootBoxEvent":
                        event_obj = MerkleLootboxV2LootBoxEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            season=int(data["season"]),
                            user=data["user"],
                            lootbox=str(data["lootbox"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- mkl_token module ---
                elif module_name == "mkl_token":
                    if event_type == "DelegateAccountVaultEvent":
                        event_obj = MerkleMklTokenDelegateAccountVaultEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            amount=int(data["amount"]),
                            event_type=int(data["event_type"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- pMKL module ---
                elif module_name == "pMKL":
                    if event_type == "ClaimEvent":
                        event_obj = MerklePmklClaimEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            season_number=int(data["season_number"]),
                            user=data["user"],
                            amount=int(data["amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "MintEvent":
                        event_obj = MerklePmklMintEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            season_number=int(data["season_number"]),
                            user=data["user"],
                            amount=int(data["amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- pre_tge_reward module ---
                elif module_name == "pre_tge_reward":
                    if event_type == "ClaimEvent":
                        event_obj = MerklePreTgeRewardClaimEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            amount=int(data["amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- profile module ---
                elif module_name == "profile":
                    if event_type == "IncreaseBoostEvent":
                        event_obj = MerkleProfileIncreaseBoostEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            boosted=str(data["boosted"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "IncreaseXPEvent":
                        event_obj = MerkleProfileIncreaseXPEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            boosted=int(data["boosted"]),
                            gained_xp=int(data["gained_xp"]),
                            xp_from=int(data["xp_from"]),
                            level_from=int(data["level_from"]),
                            class_from=int(data["class_from"]),
                            required_xp_from=int(data["required_xp_from"]),
                            xp_to=int(data["xp_to"]),
                            level_to=int(data["level_to"]),
                            class_to=int(data["class_to"]),
                            required_xp_to=int(data["required_xp_to"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "SoftResetEvent":
                        event_obj = MerkleProfileSoftResetEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            season_number=int(data["season_number"]),
                            previous_tier=int(data["previous_tier"]),
                            previous_level=int(data["previous_level"]),
                            soft_reset_tier=int(data["soft_reset_tier"]),
                            soft_reset_level=int(data["soft_reset_level"]),
                            reward_lootboxes=str(data["reward_lootboxes"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- referral module ---
                elif module_name == "referral":
                    if event_type == "ProtocolRevenueEvent":
                        event_obj = MerklereferralProtocolRevenueEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            #asset_type=json.dumps(data["asset_type"]),
                            asset_type_account_address = data["asset_type"]["account_address"],
                            asset_type_module_name = data["asset_type"]["module_name"],
                            asset_type_struct_name = data["asset_type"]["struct_name"],
                            
                            amount=int(data["amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- shard_token module ---
                elif module_name == "shard_token":
                    if event_type == "BurnEvent":
                        event_obj = MerkleshardsTokenBurnEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            amount=int(data["amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "MintEvent":
                        event_obj = MerkleshardsTokenMintEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            amount=int(data["amount"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- staking module ---
                elif module_name == "staking":
                    if event_type == "UnlockEvent":
                        event_obj = MerklestakingUnlockEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            mkl_amount=int(data["mkl_amount"]),
                            esmkl_amount=int(data["esmkl_amount"]),
                            lock_time=int(data["lock_time"]),
                            unlock_time=int(data["unlock_time"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "LockEvent":
                        event_obj = MerklestakingLockEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            #asset_type=json.dumps(data["asset_type"]),
                            asset_type_account_address = data["asset_type"]["account_address"],
                            asset_type_module_name = data["asset_type"]["module_name"],
                            asset_type_struct_name = data["asset_type"]["struct_name"],
                            
                            amount=int(data["amount"]),
                            lock_time=int(data["lock_time"]),
                            unlock_time=int(data["unlock_time"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- trading module ---
                elif module_name == "trading":
                    if event_type == "UpdateTPSLEvent":
                        event_obj = MerkleTradingUpdateTPSLEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            #pair_type=json.dumps(data["pair_type"]),
                            pair_type_account_address = data["pair_type"]["account_address"],
                            pair_type_module_name = data["pair_type"]["module_name"],
                            pair_type_struct_name = data["pair_type"]["struct_name"],
                            
                            #collateral_type=json.dumps(data["collateral_type"]),
                            collateral_type_account_address = data["collateral_type"]["account_address"],
                            collateral_type_module_name = data["collateral_type"]["module_name"],
                            collateral_type_struct_name = data["collateral_type"]["struct_name"],
                            
                            user=data["user"],
                            is_long=bool(data["is_long"]),
                            take_profit_trigger_price=int(data["take_profit_trigger_price"]),
                            stop_loss_trigger_price=int(data["stop_loss_trigger_price"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "PlaceOrderEvent":
                        event_obj = MerkleTradingPlaceOrderEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            
                            pair_type_account_address = data["pair_type"]["account_address"],
                            pair_type_module_name = data["pair_type"]["module_name"],
                            pair_type_struct_name = data["pair_type"]["struct_name"],
                            
                            #collateral_type=json.dumps(data["collateral_type"]),
                            collateral_type_account_address = data["collateral_type"]["account_address"],
                            collateral_type_module_name = data["collateral_type"]["module_name"],
                            collateral_type_struct_name = data["collateral_type"]["struct_name"],
                            
                            user=data["user"],
                            order_id=int(data["order_id"]),
                            size_delta=int(data["size_delta"]),
                            collateral_delta=int(data["collateral_delta"]),
                            price=int(data["price"]),
                            is_long=bool(data["is_long"]),
                            is_increase=bool(data["is_increase"]),
                            is_market=bool(data["is_market"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "PositionEvent":
                        event_obj = MerkleTradingPositionEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            event_type=int(data["event_type"]),
                            #pair_type=json.dumps(data["pair_type"]),
                            pair_type_account_address = data["pair_type"]["account_address"],
                            pair_type_module_name = data["pair_type"]["module_name"],
                            pair_type_struct_name = data["pair_type"]["struct_name"],
                            
                            #collateral_type=json.dumps(data["collateral_type"]),
                            collateral_type_account_address = data["collateral_type"]["account_address"],
                            collateral_type_module_name = data["collateral_type"]["module_name"],
                            collateral_type_struct_name = data["collateral_type"]["struct_name"],
                            
                            user=data["user"],
                            order_id=int(data["order_id"]),
                            is_long=bool(data["is_long"]),
                            price=int(data["price"]),
                            original_size=int(data["original_size"]),
                            size_delta=int(data["size_delta"]),
                            original_collateral=int(data["original_collateral"]),
                            collateral_delta=int(data["collateral_delta"]),
                            is_increase=bool(data["is_increase"]),
                            is_partial=bool(data["is_partial"]),
                            pnl_without_fee=int(data["pnl_without_fee"]),
                            is_profit=bool(data["is_profit"]),
                            entry_exit_fee=int(data["entry_exit_fee"]),
                            funding_fee=int(data["funding_fee"]),
                            is_funding_fee_profit=bool(data["is_funding_fee_profit"]),
                            rollover_fee=int(data["rollover_fee"]),
                            long_open_interest=int(data["long_open_interest"]),
                            short_open_interest=int(data["short_open_interest"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "CancelOrderEvent":
                        event_obj = MerkleTradingCancelOrderEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            uid=int(data["uid"]),
                            event_type=int(data["event_type"]),
                            #pair_type=json.dumps(data["pair_type"]),
                            pair_type_account_address = data["pair_type"]["account_address"],
                            pair_type_module_name = data["pair_type"]["module_name"],
                            pair_type_struct_name = data["pair_type"]["struct_name"],
                            
                            #collateral_type=json.dumps(data["collateral_type"]),
                            collateral_type_account_address = data["collateral_type"]["account_address"],
                            collateral_type_module_name = data["collateral_type"]["module_name"],
                            collateral_type_struct_name = data["collateral_type"]["struct_name"],
                            
                            user=data["user"],
                            order_id=int(data["order_id"]),
                            size_delta=int(data["size_delta"]),
                            collateral_delta=int(data["collateral_delta"]),
                            price=int(data["price"]),
                            is_long=bool(data["is_long"]),
                            is_increase=bool(data["is_increase"]),
                            is_market=bool(data["is_market"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # --- username module ---
                elif module_name == "username":
                    if event_type == "UsernameRegisterEvent":
                        event_obj = MerkleUsernameUsernameRegisterEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            name=data["name"],
                            registered_at=int(data["registered_at"]),
                            expired_at=int(data["expired_at"]),
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "TicketIssueEvent":
                        event_obj = MerkleUsernameTicketIssueEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            ticket=data["ticket"],
                            user=data["user"],
                            
                            transaction_timestamp=transaction_timestamp,
                        )
                    elif event_type == "UsernameDeleteEvent":
                        event_obj = MerkleUsernameUsernameDeleteEvent(
                            sequence_number=sequence_number,
                            creation_number=creation_number,
                            account_address=account_address,
                            transaction_version=transaction_version,
                            sender_address=sender_address,
                            identifier=identifier,
                            event_index=event_index,

                            user=data["user"],
                            name=data["name"],
                            
                            transaction_timestamp=transaction_timestamp,
                        )

                # If an event object was created, add it to our list
                if event_obj:
                    event_db_objs.append(event_obj)

        processing_duration_in_secs = perf_counter() - start_time
        db_start = perf_counter()
        self.insert_to_db(event_db_objs)
        db_insertion_duration_in_secs = perf_counter() - db_start

        return ProcessingResult(
            start_version=start_version,
            end_version=end_version,
            processing_duration_in_secs=processing_duration_in_secs,
            db_insertion_duration_in_secs=db_insertion_duration_in_secs,
        )

    def insert_to_db(self, parsed_objs: List[any]) -> None:
        if not parsed_objs:
            return
        with Session() as session, session.begin():
            for obj in parsed_objs:
                session.merge(obj)

    @staticmethod
    def included_event_type(event_type: str) -> bool:
        parsed_tag = event_type.split("::")
        module_address = general_utils.standardize_address(parsed_tag[0])
        return module_address == MODULE_ADDRESS