"""
# Developer: Richard Raphael Banak
# Objective: Example process to use when developing a new job with data quality included
# Creation date: 2022-04-16
"""

import ds_kit
from ds_kit.data_quality import process as prc

id_team = "team-name_id"
id_project = "gcp_project_id"
id_process = "0001"
ds_process = "Python process name"


def main():

    # TODO(developer): YOUR CODE GOES HERE

    print("Main Code")


if __name__ == "__main__":

    # new process instance
    process = prc.Process(
        id_team=id_team,
        id_project=id_project,
        id_process=id_process,
        ds_process=ds_process,
    )

    try:
        main()

        process.ds_execution_status = "Success"

    except Exception as e:
        process.ds_execution_status = "Error"
        process.ds_error_type = type(e).__name__
        process.ds_error_log = str(e)

    finally:
        process.finish_process()

    # if error, raise Exception
    if process.ds_error_type:
        raise Exception(process.ds_error_log)
