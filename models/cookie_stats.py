import sqlalchemy as sa
from sqlalchemy.sql import text
import typing
from utils.connect import db




class CookieStats:
    def __init__ (self, run_id, run_name, run_time):
        self.run_id = run_id
        self.run_name = run_name
        self.run_time = run_time

    @classmethod
    def query_all(cls) -> typing.List[object]:
        
        all_runs_result = db.execute("""
            SELECT run_id, run_name, run_time
            FROM cookie_stats.stats;
        """)

        all_runs = []
        for run in all_runs_result.all():
            all_runs.append(
                cls(
                    run_id = run.run_id,
                    run_name = run.run_name,
                    run_time = run.run_time
                )
            )
        return all_runs

    @classmethod
    def enter_new_run(cls, run_name, run_time):
        
        new_run = db.execute(text("""
            INSERT INTO cookie_stats.stats.start (run_name, run_time)
            VALUES (:run_name, :run_time)
            RETURNING *;
        """), run_name = run_name, run_time = run_time)

        r = new_run.one()
        run = cls(r.run_id, r.run_name, r.run_time)
        return run