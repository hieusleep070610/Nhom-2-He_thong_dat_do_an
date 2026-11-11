from sqlalchemy.orm import Session
from app.models.wallet import WalletModel
from app.schemas.wallet import WalletCreate, WalletUpdate

def get_wallet_by_id(db: Session, wallet_id: int):
    return db.query(WalletModel).filter(WalletModel.id == wallet_id).first()

def get_wallet_by_user_id(db: Session, user_id: int):
    return db.query(WalletModel).filter(WalletModel.user_id == user_id).first()

def create_wallet(db: Session, wallet_in: WalletCreate):
    db_wallet = WalletModel(
        user_id=wallet_in.user_id,
        balance=wallet_in.balance,
        xu=wallet_in.xu,
        status=wallet_in.status
    )
    db.add(db_wallet)
    db.commit()
    db.refresh(db_wallet)
    return db_wallet

def update_wallet(db: Session, db_wallet: WalletModel, wallet_in: WalletUpdate):
    update_data = wallet_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_wallet, key, value)
    db.commit()
    db.refresh(db_wallet)
    return db_wallet