import motor.motor_asyncio

from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection("students")


def student_helper(student) -> dict:
    return {
        "id": str(student["id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "gpa": student["gpa"],
    }


# Get all students
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students
