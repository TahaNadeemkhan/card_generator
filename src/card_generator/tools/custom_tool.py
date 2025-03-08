#custom_tool.py
from crewai.tools import tool
from typing import ClassVar, List
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import random

class StudentDetails(BaseModel):
  student_name: str = Field(..., description='Student name')
  student_roll_no: int = Field(..., description="Student ID")

class PiaicStudentCard(BaseTool):
  name: str = "Piaic student card generator"
  description: str = "This fucntion will create Piaic student card"
  args_schema: type[BaseModel] = StudentDetails

  def _run(self, student_name: str, student_roll_no: int) -> str:
    if student_roll_no is None:
        student_roll_no = random.randint(1000, 9999)
    return f''' 
        ****Piaic student card****
    Student name: {student_name}
    Student roll no: {student_roll_no}
        **Welcome to PIAIC!!!**
    '''
class FeesStatus(BaseModel):
    rollno: int = Field(..., description="Student roll number")

class FeesUpdate(BaseTool): 
    name: str = "Piaic student fees status manager"
    description: str =  "This fuction takes student's roll no. as input and return the fees status as paid or unpaid"
    args_schema: type[BaseModel] = FeesStatus

    dummy_data: ClassVar[List[int]] = [10, 20, 30, 40, 50, 60, 70]
    def _run(self, rollno: int) -> str:
        if rollno in self.dummy_data:
            return "Your fees is paid!"
        else:
            return "Pay your fees ASAP!"
        



