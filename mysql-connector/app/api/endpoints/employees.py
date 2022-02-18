from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.db.connection import connect

router = APIRouter()


@router.post("/create", response_class=JSONResponse)
async def create():
    try:
        name = "Simon"
        salary = 600000
        conn = connect()
        cursor = conn.cursor()
        query = "INSERT INTO employees (name, salary) VALUES (%s, %s)"
        values = (name, salary)
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Employee Created Successfully"}
    except Exception as e:
        print("[ERROR]", e)
        conn.rollback()
        return {"message": "Employee Failed to Create"}
    finally:
        cursor.close()
        conn.close()


@router.get("/", response_class=JSONResponse)
def read():
    conn = connect()
    print(conn)
    cursor = conn.cursor()
    query = "SELECT * FROM employees"
    try:
        cursor.execute(query)
        employees = cursor.fetchall()
        return JSONResponse({"employees": employees})
    except Exception as e:
        print("[ERROR]", e)
        return {"message": e}
    finally:
        cursor.close()
        conn.close()


@router.get("/{employee_id}/", response_class=JSONResponse)
async def read_by_id(employee_id: int):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "SELECT * FROM employees WHERE id = %s"
        values = (employee_id,)
        cursor.execute(query, values)
        employee = cursor.fetchone()

        if employee == None:
            raise Exception("Employee Does Not Exists")
        return JSONResponse({"employee": employee})
    except Exception as e:
        print("[ERROR]", e)
        return {"message": e}
    finally:
        cursor.close()
        conn.close()


@router.delete("/{employee_id}", response_class=JSONResponse)
async def delete(employee_id: int):
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM employees WHERE id= %s"
    values = (employee_id,)
    try:
        cursor.execute(query, values)
        conn.commit()
        return JSONResponse({"message": "Employee Deleted Successfully"})
    except Exception as e:
        print("[ERROR]", e)
        return {"message": e}
    finally:
        cursor.close()
        conn.close()


@router.put("/{employee_id}", response_class=JSONResponse)
async def update(employee_id: int):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE employees set salary = %s WHERE id = %s"
    values = (9999, employee_id)
    try:
        cursor.execute(query, values)
        conn.commit()
        return JSONResponse({"message": "Employee Updated Sucessfully"})
    except Exception as e:
        print("[ERROR]", e)
        return {"message": e}
    finally:
        cursor.close()
        conn.close()
