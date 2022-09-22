HMS (Hospitals Management System):

> Create new module called "hms"
> Create a model for patient called "hms.patient"
> Create needed menus to view/create patients' data
> The model contains the following data:

> First name
> Last name
> Birth date
> History (html)
> CR Ratio (float)
> Blood type (drop down)
> PCR (checkbox)
> Image (upload image)
> Address (text)
> Age

> Continue with our previously created module "hms"
> Create a model for departments called "hms.department"
> Create a model for doctors called "hms.doctors"
> Create needed menus to view/create departments' and doctors' data

> Department model contains the following:

> Name
> Capacity (integer)
> Is_opened (boolean)
> Patients
> Doctors model contains the following:
> First Name
> Last Name
> Image

> The patient model should be linked to department and doctors and the selected department capacity should be shown from the patient view too.
> Add new log history for the patient
> The log record shows the following date:
> Created by, Date, description
> The patient should have a states (Undetermined, Good, Fair, Serious)
> With each change of the state a new log record is being created with a description of (State changed to NEW_STATE)

> The patient can't choose a closed department
> The Doctors field is a many2many tags and should be
> readonly until the department is being selected
> The first name and last name are required
> If The pcr field is checked, the CR ratio field should be mandatory
> The history field should be hidden if the age is less than 50
> The PCR field should be automatically checked if the age is lower than 30 and show a warning message that it has been checked

> Continue with our previously created module "hms"
> Add email field to patients' model and make sure that it is a valid and unique email address
> Link patient model with customers model from CRM module by adding a new field in customers model called "related_patient_id" and show this field inside Misc group within sales and purchase tab

> Convert the patient's age field to be auto calculated based on birth date
> Add a constraint on CRM customer model which prevents linking patient with email that is already assigned to a different customer.
> Prevent users to delete any customer linked to a patient
> Show website field in the list view for customers
> Make the Tax ID field mandatory for CRM Customers

> Continue with our previously created module "hms"
> Create two new user groups (user , manager)
> The user group has the following access rights:
> Can create/read/update his own patients records
> Can read only departments
> Can read only doctors
> Can't view doctor fields in patients' form view
> Can't view doctors' menu item

> The Manager group has the following access rights:
> Can create/read/update/delete all patients records
> Can create/read/update/delete departments
> Can create/read/update/delete doctors
> Can view doctor fields in patients form view
> Can view doctors menu item

> Create a patients report like the following design Patient Status Report

Name: Patient's name
Age: 25
Department: department name
Doctors: doctor1, doctor2, doctor2

Birth date: 12/10/1995
PCR: 2.5
Blood Type: A+
Email: patient@test.com

Log History
