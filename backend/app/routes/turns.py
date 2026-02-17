from fastapi import APIRouter

router = APIRouter(prefix="/turns", tags=["Turns"])

@router.get("/")
def test_route():
    return {"message": "Turns router funcionando"}
