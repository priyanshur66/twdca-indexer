from utils.models.annotated_types import (
    StringType,
    BigIntegerType,
    BigIntegerPrimaryKeyType,
    BooleanType,
    InsertedAtType,
    NumericType,
    StringPrimaryKeyType,
    TimestampType,
    NullableNumericType,
    NullableStringType,
)
from utils.models.general_models import Base
from utils.models.schema_names import MERKLE_SCHEMA_NAME

# Delegate Account Events
class MerkleDelegateAccountDelegateAccountVaultEvent(Base):
    __tablename__ = "merkle_delegate_account_delegateaccountvaultevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    amount : NumericType
    event_type : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType


class MerkleDelegateAccountRegisterEvent(Base):
    __tablename__ = "merkle_delegate_account_registerevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    referrer : StringType
    referee : StringType
    registered_at : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleDelegateAccountClaimEvent(Base):
    __tablename__ = "merkle_delegate_account_claimevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    amount : NumericType
    epoch : NumericType
    extras : StringType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleDelegateAccountRebateEvent(Base):
    __tablename__ = "merkle_delegate_account_rebateevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    referrer : StringType
    referee : StringType
    rebate : NumericType
    rebate_rate : NumericType
    epoch : NumericType
    extras : StringType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# Fee Distributor Events
class MerkleFeeDistributorDepositFeeEvent(Base):
    __tablename__ = "merkle_fee_distributor_depositfeeevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    lp_amount : NumericType
    stake_amount : NumericType
    dev_amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# Gear Events
class MerkleGearEquipEvent(Base):
    __tablename__ = "merkle_gear_equipevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    uid : NumericType
    gear_address : StringType
    user : StringType
    durability : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleGearGearEffectEvent(Base):
    __tablename__ = "merkle_gear_geareffectevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    uid : NumericType
    gear_address : StringType
    #pair_type : StringType  # TypeInfo is represented as string
    pair_type_account_address : StringType
    pair_type_module_name : StringType
    pair_type_struct_name: StringType
    
    user : StringType
    effect : NumericType
    gear_type : NumericType
    gear_code : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleGearUnequipEvent(Base):
    __tablename__ = "merkle_gear_unequipevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    uid : NumericType
    gear_address : StringType
    user : StringType
    durability : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleGearSalvageEvent(Base):
    __tablename__ = "merkle_gear_salvageevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    uid : NumericType
    gear_address : StringType
    shard_amount : NumericType
    user : StringType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleGearRepairEvent(Base):
    __tablename__ = "merkle_gear_repairevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    uid : NumericType
    gear_address : StringType
    shard_amount : NumericType
    user : StringType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleGearMintEvent(Base):
    __tablename__ = "merkle_gear_mintevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    uid : NumericType
    gear_address : StringType
    season : NumericType
    user : StringType
    name : StringType
    uri : StringType
    gear_type : NumericType
    gear_code : NumericType
    tier : NumericType
    primary_effect : NumericType
    gear_affixes : StringType  # vector<GearAffix> represented as string
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleGearForgeEvent(Base):
    __tablename__ = "merkle_gear_forgeevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    gear1_uid : NumericType
    gear1_address : StringType
    gear2_uid : NumericType
    gear2_address : StringType
    required_shard : NumericType
    gear_tier : NumericType
    result_tier : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType
    
    
# House LP Events
class MerkleHouseLpRedeemEvent(Base):
    __tablename__ = "merkle_house_lp_redeem_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    #asset_type : StringType
    asset_type_account_address : StringType
    asset_type_module_name : StringType
    asset_type_struct_name : StringType
    
    burn_amount : NumericType
    withdraw_amount : NumericType
    redeem_amount_left : NumericType
    withdraw_fee : NumericType
    started_at_sec : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleHouseLpFeeEvent(Base):
    __tablename__ = "merkle_house_lp_fee_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    fee_type : NumericType
    
    #asset_type : StringType
    asset_type_account_address : StringType
    asset_type_module_name : StringType
    asset_type_struct_name : StringType
    
    amount : NumericType
    amount_sign : BooleanType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# class MerkleHouseLpDepositEvent(Base):
#     __tablename__ = "merkle_house_lp_deposit_event"
#     __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
#     sequence_number : BigIntegerType
#     creation_number : BigIntegerType
#     account_address : StringType
#     sender_address : StringType
#     transaction_version : BigIntegerType
#     identifier : BigIntegerPrimaryKeyType
#     event_index : BigIntegerType
    
#     #asset_type : StringType
#     asset_type_account_address : StringType
#     asset_type_module_name : StringType
#     asset_type_struct_name : StringType
    
#     user : StringType
#     deposit_amount : NumericType
#     mint_amount : NumericType
#     deposit_fee : NumericType
    
#     transaction_timestamp : TimestampType
#     inserted_at : InsertedAtType

class MerkleHouseLpRedeemCancelEvent(Base):
    __tablename__ = "merkle_house_lp_redeem_cancel_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    return_amount : NumericType
    initial_amount : NumericType
    started_at_sec : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleHouseLpDepositEvent(Base):
    __tablename__ = "merkle_house_lp_depositEvent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
     
    #asset_type : StringType
    asset_type_account_address : StringType
    asset_type_module_name : StringType
    asset_type_struct_name : StringType    
        
    user: StringType
    deposit_amount: NumericType
    mint_amount: NumericType
    deposit_fee: NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# Liquidity Auction Events
class MerkleLiquidityAuctionWithdrawAssetEvent(Base):
    __tablename__ = "merkle_liquidity_auction_withdraw_asset_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    #asset_type : StringType
    asset_type_account_address : StringType
    asset_type_module_name : StringType
    asset_type_struct_name : StringType    
    
    asset_withdraw_amount : NumericType
    asset_total_amount : NumericType
    phase1_asset_deposit_amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleLiquidityAuctionDepositPreMklEvent(Base):
    __tablename__ = "merkle_liquidity_auction_deposit_pre_mkl_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    pre_mkl_deposit_amount : NumericType
    total_pre_mkl_deposit_amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleLiquidityAuctionDepositAssetEvent(Base):
    __tablename__ = "merkle_liquidity_auction_deposit_asset_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    #asset_type : StringType
    asset_type_account_address : StringType
    asset_type_module_name : StringType
    asset_type_struct_name : StringType
    
    asset_deposit_amount : NumericType
    phase1_asset_deposit_amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# Lootbox Events
class MerkleLootboxLootBoxOpenEvent(Base):
    __tablename__ = "merkle_lootbox_lootbox_open_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    tier : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleLootboxLootBoxEvent(Base):
    __tablename__ = "merkle_lootbox_lootbox_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    lootbox : StringType  # Since it's a vector in Move, we'll store it as a string
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# Lootbox V2 Events
class MerkleLootboxV2LootBoxOpenEvent(Base):
    __tablename__ = "merkle_lootbox_v2_lootbox_open_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    season : NumericType
    user : StringType
    tier : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleLootboxV2FtuLootBoxEvent(Base):
    __tablename__ = "merkle_lootbox_v2_ftu_lootbox_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    reward_tier : NumericType
    referrer : StringType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleLootboxV2LootBoxEvent(Base):
    __tablename__ = "merkle_lootbox_v2_lootbox_event"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    season : NumericType
    user : StringType
    lootbox : StringType  # Since it's a vector in Move, we'll store it as a string
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType
    
    
# MKL Token Module Events
class MerkleMklTokenDelegateAccountVaultEvent(Base):
    __tablename__ = "merklemkl_token_delegateaccountvaultevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}

    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    amount : NumericType
    event_type : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# pMKL Module Events
class MerklePmklClaimEvent(Base):
    __tablename__ = "merklepmkl_claimevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}

    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    season_number : NumericType
    user : StringType
    amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerklePmklMintEvent(Base):
    __tablename__ = "merklepmkl_mintevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}

    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    season_number : NumericType
    user : StringType
    amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# Pre TGE Reward Module Events
class MerklePreTgeRewardClaimEvent(Base):
    __tablename__ = "merklepre_tge_reward_claimevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}

    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# Profile Module Events
class MerkleProfileIncreaseBoostEvent(Base):
    __tablename__ = "merkleprofile_increaseboostevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}

    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    boosted : StringType  # Storing vector<u64> as a string representation
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleProfileIncreaseXPEvent(Base):
    __tablename__ = "merkleprofile_increasexpevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}

    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    boosted : NumericType
    gained_xp : NumericType
    xp_from : NumericType
    level_from : NumericType
    class_from : NumericType
    required_xp_from : NumericType
    xp_to : NumericType
    level_to : NumericType
    class_to : NumericType
    required_xp_to : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleProfileSoftResetEvent(Base):
    __tablename__ = "merkleprofile_softresetevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}

    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    season_number : NumericType
    previous_tier : NumericType
    previous_level : NumericType
    soft_reset_tier : NumericType
    soft_reset_level : NumericType
    reward_lootboxes : StringType  # Storing vector<u64> as a string representation
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType
    
    
# Referral Module Events
class MerklereferralProtocolRevenueEvent(Base):
    __tablename__ = "merklereferral_protocolrevenueevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    
    #asset_type : StringType
    asset_type_account_address : StringType
    asset_type_module_name : StringType
    asset_type_struct_name : StringType
    
    amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType


# Shard Token Module Events
class MerkleshardsTokenBurnEvent(Base):
    __tablename__ = "merkleshard_token_burnevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerkleshardsTokenMintEvent(Base):
    __tablename__ = "merkleshard_token_mintevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    amount : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

# Staking Module Events
class MerklestakingUnlockEvent(Base):
    __tablename__ = "merklestaking_unlockevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    mkl_amount : NumericType
    esmkl_amount : NumericType
    lock_time : NumericType
    unlock_time : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType

class MerklestakingLockEvent(Base):
    __tablename__ = "merklestaking_lockevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number : BigIntegerType
    creation_number : BigIntegerType
    account_address : StringType
    sender_address : StringType
    transaction_version : BigIntegerType
    identifier : BigIntegerPrimaryKeyType
    event_index : BigIntegerType
    
    user : StringType
    
    #asset_type : StringType
    asset_type_account_address : StringType
    asset_type_module_name : StringType
    asset_type_struct_name : StringType
    
    amount : NumericType
    lock_time : NumericType
    unlock_time : NumericType
    
    transaction_timestamp : TimestampType
    inserted_at : InsertedAtType
    
    
# Trading Module Events
class MerkleTradingUpdateTPSLEvent(Base):
    __tablename__ = "merkle_trading_updatetpslevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number: BigIntegerType
    creation_number: BigIntegerType
    account_address: StringType
    sender_address: StringType
    transaction_version: BigIntegerType
    identifier: BigIntegerPrimaryKeyType
    event_index: BigIntegerType
    
    uid: NumericType
    
    # #asset_type : StringType
    # asset_type_account_address : StringType
    # asset_type_module_name : StringType
    # asset_type_struct_name : StringType
    
    #pair_type: StringType
    pair_type_account_address : StringType
    pair_type_module_name : StringType
    pair_type_struct_name : StringType
    
    #collateral_type: StringType
    collateral_type_account_address: StringType
    collateral_type_module_name: StringType
    collateral_type_struct_name: StringType
    
    user: StringType
    is_long: BooleanType
    take_profit_trigger_price: NumericType
    stop_loss_trigger_price: NumericType
    
    transaction_timestamp: TimestampType
    inserted_at: InsertedAtType


class MerkleTradingPlaceOrderEvent(Base):
    __tablename__ = "merkle_trading_placeorderevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number: BigIntegerType
    creation_number: BigIntegerType
    account_address: StringType
    sender_address: StringType
    transaction_version: BigIntegerType
    identifier: BigIntegerPrimaryKeyType
    event_index: BigIntegerType
    
    uid: NumericType
    
    #pair_type: StringType
    pair_type_account_address : StringType
    pair_type_module_name : StringType
    pair_type_struct_name : StringType
    
    #collateral_type: StringType
    collateral_type_account_address: StringType
    collateral_type_module_name: StringType
    collateral_type_struct_name: StringType
    
    user: StringType
    order_id: NumericType
    size_delta: NumericType
    collateral_delta: NumericType
    price: NumericType
    is_long: BooleanType
    is_increase: BooleanType
    is_market: BooleanType
    
    transaction_timestamp: TimestampType
    inserted_at: InsertedAtType


class MerkleTradingPositionEvent(Base):
    __tablename__ = "merkle_trading_positionevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number: BigIntegerType
    creation_number: BigIntegerType
    account_address: StringType
    sender_address: StringType
    transaction_version: BigIntegerType
    identifier: BigIntegerPrimaryKeyType
    event_index: BigIntegerType
    
    uid: NumericType
    event_type: NumericType
    
    #pair_type: StringType
    pair_type_account_address : StringType
    pair_type_module_name : StringType
    pair_type_struct_name : StringType
    
    #collateral_type: StringType
    collateral_type_account_address: StringType
    collateral_type_module_name: StringType
    collateral_type_struct_name: StringType
    
    user: StringType
    order_id: NumericType
    is_long: BooleanType
    price: NumericType
    original_size: NumericType
    size_delta: NumericType
    original_collateral: NumericType
    collateral_delta: NumericType
    is_increase: BooleanType
    is_partial: BooleanType
    pnl_without_fee: NumericType
    is_profit: BooleanType
    entry_exit_fee: NumericType
    funding_fee: NumericType
    is_funding_fee_profit: BooleanType
    rollover_fee: NumericType
    long_open_interest: NumericType
    short_open_interest: NumericType
    
    transaction_timestamp: TimestampType
    inserted_at: InsertedAtType


class MerkleTradingCancelOrderEvent(Base):
    __tablename__ = "merkle_trading_cancelorderevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number: BigIntegerType
    creation_number: BigIntegerType
    account_address: StringType
    sender_address: StringType
    transaction_version: BigIntegerType
    identifier: BigIntegerPrimaryKeyType
    event_index: BigIntegerType
    
    uid: NumericType
    event_type: NumericType
    pair_type_account_address : StringType
    pair_type_module_name : StringType
    pair_type_struct_name : StringType
    #collateral_type: StringType
    collateral_type_account_address: StringType
    collateral_type_module_name: StringType
    collateral_type_struct_name: StringType
    user: StringType
    order_id: NumericType
    size_delta: NumericType
    collateral_delta: NumericType
    price: NumericType
    is_long: BooleanType
    is_increase: BooleanType
    is_market: BooleanType
    
    transaction_timestamp: TimestampType
    inserted_at: InsertedAtType


# Username Module Events
class MerkleUsernameUsernameRegisterEvent(Base):
    __tablename__ = "merkle_username_usernameregisterevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number: BigIntegerType
    creation_number: BigIntegerType
    account_address: StringType
    sender_address: StringType
    transaction_version: BigIntegerType
    identifier: BigIntegerPrimaryKeyType
    event_index: BigIntegerType
    
    user: StringType
    name: StringType
    registered_at: NumericType
    expired_at: NumericType
    
    transaction_timestamp: TimestampType
    inserted_at: InsertedAtType


class MerkleUsernameTicketIssueEvent(Base):
    __tablename__ = "merkle_username_ticketissueevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number: BigIntegerType
    creation_number: BigIntegerType
    account_address: StringType
    sender_address: StringType
    transaction_version: BigIntegerType
    identifier: BigIntegerPrimaryKeyType
    event_index: BigIntegerType
    
    ticket: StringType
    user: StringType
    
    transaction_timestamp: TimestampType
    inserted_at: InsertedAtType


class MerkleUsernameUsernameDeleteEvent(Base):
    __tablename__ = "merkle_username_usernamedeleteevent"
    __table_args__ = {"schema": MERKLE_SCHEMA_NAME}
    
    sequence_number: BigIntegerType
    creation_number: BigIntegerType
    account_address: StringType
    sender_address: StringType
    transaction_version: BigIntegerType
    identifier: BigIntegerPrimaryKeyType
    event_index: BigIntegerType
    
    user: StringType
    name: StringType
    
    transaction_timestamp: TimestampType
    inserted_at: InsertedAtType