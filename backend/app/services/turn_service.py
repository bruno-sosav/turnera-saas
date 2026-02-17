from sqlalchemy.orm import Session
from app.models.turn import Turn

def create_turn(db: Session, client_name: str, service: str, date):
    turn = Turn(
        client_name=client_name,
        service=service,
        date=date
    )
    db.add(turn)
    db.commit()
    db.refresh(turn)
    return turn


def get_turns(db: Session):
    return db.query(Turn).all()
