import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Page title
st.set_page_config(page_title='ACOM CORP', page_icon='💻')
st.title('💻 Config to OLT ACOM')
st.info('Cấu hình tự động OLT các dự án của ACOM trên toàn quốc và kiểm tra số lượng thuê bao đang tồn tại.')

# Generate data
np.random.seed(42)

def generate_issue():
    issues = [
        "Network connectivity issues in the office",
        "Software application crashing on startup",
        "Printer not responding to print commands",
        "Email server downtime",
        "Data backup failure",
        "Login authentication problems",
        "Website performance degradation",
        "Security vulnerability identified",
        "Hardware malfunction in the server room",
        "Employee unable to access shared files",
        "Database connection failure",
        "Mobile application not syncing data",
        "VoIP phone system issues",
        "VPN connection problems for remote employees",
        "System updates causing compatibility issues",
        "File server running out of storage space",
        "Intrusion detection system alerts",
        "Inventory management system errors",
        "Customer data not loading in CRM",
        "Collaboration tool not sending notifications"
    ]
    return np.random.choice(issues)

start_date = datetime(2023, 6, 1)
end_date = datetime(2023, 12, 20)
id_values = ['TICKET-{}'.format(i) for i in range(1000, 1100)]
issue_list = [generate_issue() for _ in range(100)]

def generate_random_dates(start_date, end_date, id_values):
    date_range = pd.date_range(start_date, end_date).strftime('%m-%d-%Y')
    return np.random.choice(date_range, size=len(id_values), replace=False)

data = {'Issue': issue_list,
        'Status': np.random.choice(['Open', 'In Progress', 'Closed'], size=100),
        'Priority': np.random.choice(['High', 'Medium', 'Low'], size=100),
        'Date Submitted': generate_random_dates(start_date, end_date, id_values)
    }
df = pd.DataFrame(data)
df.insert(0, 'ID', id_values)
df = df.sort_values(by=['Status', 'ID'], ascending=[False, False])

if 'df' not in st.session_state:
    st.session_state.df = df

def sort_df():
    st.session_state.df = edited_df.copy().sort_values(by=['Status', 'ID'], ascending=[False, False])

# Main content
project_options = ['Dự án 1', 'Dự án 2', 'Dự án 3']
selected_project = st.selectbox('Chọn dự án', project_options)

if selected_project:
    st.write(f'Bạn đã chọn dự án: {selected_project}')
    st.write('Đang chuyển đến giao diện cấu hình OLT...')
    # TODO: Thêm logic để chuyển đến giao diện cấu hình OLT

recent_ticket_number = int(max(st.session_state.df.ID).split('-')[1])
st.write(f'Số lượng thuê bao hiện tại: {recent_ticket_number - 1000}')
