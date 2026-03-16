from pydantic import BaseModel , EmailStr , Field , field_validator
from typing import List , Dict , Optional

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float = Field(gt=0)
    married : bool
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls , value):
        valid_domains = ["icici.com" , "hdfc.com"]
        domain_name = value.split("@")[-1]
        if domain_name in valid_domains:
            return value
        else:
            raise ValueError('Not a valid domain')
        
    @field_validator("name")
    @classmethod
    def transform_name(cls , value):
        return value.upper()



def insert_patient_data(patient1 : Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.email)
    # print(patient1.weight)
    # print(patient1.married)
    # print(patient1.allergies)
    # print(patient1.contact_details)
    print("data inserted")

patient_info = {"name" : "ayush" ,"email":"agcg@hdfc.com" , "age" : "19" , "weight":78.92 , "married" : False , "allergies" : ["dust" , "peanut"] , "contact_details" : {"email" : "abc@gmail.com" , "phone" : "5968492028"}} 

patient1 = Patient(**patient_info)

insert_patient_data(patient1)


