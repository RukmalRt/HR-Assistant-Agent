from mcp.server.fastmcp import FastMCP
from hrms import *
from email_sender import EmailSender
from utils import seed_services
import os
from dotenv import load_dotenv
from datetime import datetime

email_sender = EmailSender(
    smtp_server="smtp.gmail.com",
    port=587,
    username=os.getenv("CB_EMAIL"),
    password=os.getenv("CB_EMAIL_PWD"),
    use_tls=True
)

mcp = FastMCP("atliq-hr-assist")

employee_manager = EmployeeManager()
leave_manager = LeaveManager()
ticket_manager = TicketManager()
meeting_manager = MeetingManager()

seed_services(employee_manager, leave_manager, meeting_manager, ticket_manager)
# tools
# resources
# prompts

@mcp.tool()
def add_employee(emp_name:str, manager_id: str, email: str) -> str:
    """"
    Add a new employee to the HRMS system.
    :param emp_name: Employee name
    :param manager_id: Manager ID (optional)
    :return: Confirmation message
    """

    emp = EmployeeCreate(
        emp_id = employee_manager.get_next_emp_id(),
        name = emp_name,
        manager_id = manager_id,
        email = email
    )
    employee_manager.add_employee(emp)
    return f"Employee {emp_name} added successfully"

@mcp.tool()
def get_employee_details(name: str) -> dict[str, str]:
    """
    Get employee details by name.
    :param name: Name of employee
    :return: Employee ID and manager ID
    """

    matches = employee_manager.search_employee_by_name(name)
    if len(matches) == 0:
        raise ValueError(f"No employees found matching {name}")
    emp_id = matches[0]
    return employee_manager.get_employee_details(emp_id)

@mcp.tool()
def send_email(subject:str, body: str, to_emails: list[str]):
    email_sender.send_email(
        subject=subject,
        body= body,
        to_emails=to_emails,
        from_email=email_sender.username
    )
    return "Email sent successfully"

@mcp.tool()
def create_ticket(emp_id: str, item: str, reason: str):
    ticket_req = TicketCreate(
        emp_id=emp_id,
        item=item,
        reason=reason
    )
    return ticket_manager.create_ticket(ticket_req)

@mcp.tool()
def schedule_meeting(emp_id: str, dt_str: str, topic:str):
    try:
        meeting_dt = datetime.fromisoformat(dt_str)
    except ValueError:
        raise ValueError("Invalid datetime format; use ISO format, e.g., 2025-12-25T14:30:00")
    meeting_req = MeetingCreate(
        emp_id=emp_id,
        meeting_dt=meeting_dt,
        topic=topic
    )
    return meeting_manager.schedule_meeting(meeting_req)

@mcp.tool()
def add_leave(emp_id: str, leave_dates: str):
    """
        leave_dates: comma-separated string of ISO dates, e.g., "2025-12-25,2025-12-26"
    """
    try:
        dates_list = [datetime.fromisoformat(d.strip()) for d in leave_dates.split(",")]
    except ValueError:
        raise ValueError("Invalid date format. Use ISO format, e.g., 2025-12-25")

    new_leave = LeaveApplyRequest(
        emp_id = emp_id,
        leave_dates = leave_dates
    )
    return leave_manager.apply_leave(new_leave)

@mcp.prompt("onboard_new_employee")
def onboard_new_employee(employee_name: str, manager_name: str):
    return f""""
        Onboard a new employee with the following details:
        - Name: {employee_name}
        - Manager Name: {manager_name}
        Steps to follow:
        - Add the employee to the HRMS system.
        - Send a welcome email to the employee with their login credentials. (login format: Employee ID and Password:employee_id1234)
        - Notify the manager about new employee's onboarding.
        - Raise tickets for a new laptop, id card, and other necessary equipment.
"""





@mcp.resource("http://localhost/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    mcp.run(transport="stdio")