from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.wallet import WalletCreate, WalletOut, WalletUpdate
from app.crud import wallet as crud_wallet

router_wallet = APIRouter(prefix="/api/wallets", tags=["Wallets"])

@router_wallet.get("/{wallet_id}", response_model=WalletOut)
def get_wallet(wallet_id: int, db: Session = Depends(get_db)):
    db_wallet = crud_wallet.get_wallet_by_id(db, wallet_id=wallet_id)
    if not db_wallet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy ví tiền")
    return db_wallet

@router_wallet.post("/", response_model=WalletOut, status_code=status.HTTP_201_CREATED)
def create_wallet(wallet_in: WalletCreate, db: Session = Depends(get_db)):
    existing = crud_wallet.get_wallet_by_user_id(db, user_id=wallet_in.user_id)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Người dùng này đã có ví rồi")
    return crud_wallet.create_wallet(db, wallet_in=wallet_in)

@router_wallet.put("/{wallet_id}", response_model=WalletOut)
def update_wallet(wallet_id: int, wallet_in: WalletUpdate, db: Session = Depends(get_db)):
    db_wallet = crud_wallet.get_wallet_by_id(db, wallet_id=wallet_id)
    if not db_wallet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy ví tiền")
    return crud_wallet.update_wallet(db, db_wallet=db_wallet, wallet_in=wallet_in)