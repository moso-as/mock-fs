from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.middleware.cors import CORSMiddleware
from data_sets import add_activities, add_members, add_termin


app = FastAPI()

origins = ["*"]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

DATABASE_URL = "sqlite:///./activities.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Activity(Base):
    __tablename__ = "activities"

    id = Column(String, primary_key=True, index=True)
    emne_institusjon = Column(Integer, nullable=False)
    emne_kode = Column(String, nullable=False)
    emne_versjon = Column(String, nullable=False)
    semester_ar = Column(Integer, nullable=False)
    semester_termin = Column(String, nullable=False)
    termin_nummer = Column(Integer, nullable=False)
    aktivitet = Column(String, nullable=False)
    disiplin = Column(String, nullable=False)
    navn = Column(String, nullable=False)
    praksis_days = Column(Integer, nullable=True)
    perioder_fraDato = Column(String, nullable=True)
    perioder_tilDato = Column(String, nullable=True)
    period = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

class Member(Base):
    __tablename__ = "members"

    id = Column(String, primary_key=True)
    epost = Column(String, primary_key=True)
    role = Column(String, nullable=False)
    plnr = Column(Integer, nullable=False)
    user_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    student_nummer = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

class Termin(Base):
    __tablename__ = "termin"
    year = Column(String, primary_key=True)
    termin = Column(String, primary_key=True)

Base.metadata.create_all(bind=engine)
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/activities/")
async def create_activity(activity: dict, db: Session = Depends(get_db)):
    """
    Create a new activity.

    **Required Parameters:**
    - `id` (str): Unique identifier for the activity.
    - `emne_institusjon` (int): Institution code.
    - `emne_kode` (str): Course code.
    - `emne_versjon` (str): Course version.
    - `semester_ar` (int): Year of the semester (e.g., 2026).
    - `semester_termin` (str): Term of the semester (e.g., "VÅR" for spring).
    - `termin_nummer` (int): Term number.
    - `aktivitet` (str): Activity identifier.
    - `disiplin` (str): Discipline type.
    - `navn` (str): Activity name.

    **Optional Parameters:**
    - `praksis_days` (int | None): Number of practice days.
    - `perioder_fraDato` (str | None): Start date of the period.
    - `perioder_tilDato` (str | None): End date of the period.
    - `period` (str | None): Period description.

    """
    db_activity = Activity(**activity)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

@app.get("/activities_by_termin/")
async def get_activities(db: Session = Depends(get_db)):
    # Get current termin
    current_termin = db.query(Termin).first()
    if not current_termin:
        raise HTTPException(status_code=404, detail="Termin not found")
        
    # Query activities matching current year and semester
    activities = db.query(Activity).filter(
        Activity.semester_ar == int(current_termin.year),
        Activity.semester_termin == current_termin.termin
    ).all()
    
    return {"total": len(activities), "activities": activities}

@app.get("/activities_all/")
async def get_activity(db: Session = Depends(get_db)):
    activities = db.query(Activity).all()
    if not activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    return {"total": len(activities), "activities": activities}

@app.put("/activities/{activity_id}")
async def update_activity(activity_id: str, updated_activity: dict, db: Session = Depends(get_db)):
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    for key, value in updated_activity.items():
        setattr(activity, key, value)
    db.commit()
    db.refresh(activity)
    return activity

@app.delete("/activities/{activity_id}", 
    response_model=dict,
    summary="Delete an activity",
    description="Deletes an activity by its ID"
)
async def delete_activity(activity_id: str, db: Session = Depends(get_db)):
    """
    Delete an activity with the specified ID.

    Parameters:
    - **activity_id**: The unique identifier of the activity to delete

    Returns:
    - A message confirming the deletion
    
    Raises:
    - 404: If the activity is not found
    - 400: If there's an error during deletion
    """
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if not activity:
        raise HTTPException(
            status_code=404,
            detail=f"Activity with ID {activity_id} not found"
        )
    
    try:
        db.delete(activity)
        db.commit()
        return {
            "status": "success",
            "message": f"Activity with ID {activity_id} has been deleted"
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Error deleting activity: {str(e)}"
        )


@app.post("/members/")
async def create_member(member: dict, db: Session = Depends(get_db)):
    db_member = Member(**member)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

@app.get("/members/")
async def get_members(db: Session = Depends(get_db)):
    members = db.query(Member).all()
    return {"total": len(members), "members": members}

@app.get("/members/{member_id}")
async def get_member(member_id: str, db: Session = Depends(get_db)):
    members = db.query(Member).filter(Member.id == member_id).all()
    if not members:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"total": len(members), "members": members}

@app.put("/members/{member_id}")
async def update_member(member_id: str, updated_member: dict, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    for key, value in updated_member.items():
        setattr(member, key, value)
    db.commit()
    db.refresh(member)
    return member

@app.delete("/members/{member_id}",
    response_model=dict,
    summary="Delete a member",
    description="Deletes a member by their ID"
)
async def delete_member(member_id: str, db: Session = Depends(get_db)):
    """
    Delete a member with the specified ID.

    Parameters:
    - **member_id**: The unique identifier of the member to delete

    Returns:
    - A message confirming the deletion
    
    Raises:
    - 404: If the member is not found
    - 400: If there's an error during deletion
    """
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(
            status_code=404,
            detail=f"Member with ID {member_id} not found"
        )
    
    try:
        db.delete(member)
        db.commit()
        return {
            "status": "success",
            "message": f"Member with ID {member_id} has been deleted"
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Error deleting member: {str(e)}"

        )
    
@app.put("/termin/")
async def update_termin(year: str, termin: str, db: Session = Depends(get_db)):
    """
    Update termin.

    Available years  => 2025 or 2026  termins HØST, VÅR

    """
    existing_termin = db.query(Termin).first()
    if not existing_termin:
        raise HTTPException(status_code=404, detail="Termin not found")
    existing_termin.year = year
    existing_termin.termin = termin   
    db.commit()
    db.refresh(existing_termin)
    return existing_termin

@app.get("/termin/")
async def get_termin(db: Session = Depends(get_db)):
    termin = db.query(Termin).first()
    return {"year": termin.year, "termin": termin.termin}

