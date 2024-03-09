from typing import List

from . import models, schemas

from sqlalchemy.orm import Session


def get_all_versions(db: Session, version_id):
    return db.query(models.Version).filter(models.Version.id == version_id).first()

def get_latest_version_number(db: Session)

def get_dependencies(db: Session, version_id, skip: int = 0):
    return db.query(models.Version.dependencies).offset(skip).all()

def create_version(db: Session, version: schemas.VersionCreate, dependency_ids: List[schemas.Item]):
    db_version = models.Version(number=version.number)