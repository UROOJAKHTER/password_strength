import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        .stTextInput > div, button {
            cursor: pointer !important;
        }

        .stTextInput input {
            padding: 0.75rem;
            font-size: 16px;
            border-radius: 8px;
        }

        .stApp {
            background-color: #f9f9f9;
            padding-top: 2rem;
        }

        .main-title {
            font-size: 32px;
            font-weight: bold;
            color: #333333;
            text-align: center;
            padding-bottom: 1rem;
        }

        .strength-box {
            font-size: 20px;
            font-weight: bold;
            padding: 12px;
            border-radius: 10px;
            margin-top: 20px;
        }

        .weak { background-color: #ffdddd; color: #d60000; }
        .moderate { background-color: #fff5cc; color: #996c00; }
        .strong { background-color: #ddffdd; color: #006600; }
    </style>
""", unsafe_allow_html=True)

# Function to evaluate password
def evaluate_password(password: str):
    score = 0
    feedback = []
    specials = "!@#$%^&*"

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if any(c in specials for c in password):
        score += 1
    else:
        feedback.append("Use a special character (!@#$%^&*).")

    return score, feedback

# Determine strength label
def get_strength(score):
    if score <= 2:
        return "Weak", "weak"
    elif score <= 4:
        return "Moderate", "moderate"
    else:
        return "Strong", "strong"

# App UI
st.markdown('<div class="main-title">Password Strength Meter</div>', unsafe_allow_html=True)

password = st.text_input("Enter your password", type="password")

if password:
    score, tips = evaluate_password(password)
    strength_label, strength_class = get_strength(score)

    st.markdown(
        f'<div class="strength-box {strength_class}">Strength: {strength_label} ({score}/5)</div>',
        unsafe_allow_html=True
    )

    if strength_label != "Strong":
        st.subheader("How to improve your password:")
        for tip in tips:
            st.write(f"- {tip}")
    else:
        st.success("Your password is strong and meets all security requirements.")