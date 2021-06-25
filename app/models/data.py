from app import db


class Data(db.Model):
    __tablename__ = 'data'

    id =
    quantity_id =
    timestamp_from =
    timestamp_to =
    mean =
    min =
    max =
    stdev =
    records =

    def __repr__(self):
        return '{}'.format(self.name)