import streamlit as st
from zxcvbn import zxcvbn

# Function to load Tailwind CSS using CDN
def load_tailwind_css():
    st.markdown(
        """
        <style>
        @import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.0.0/dist/tailwind.min.css');
        </style>
        """, unsafe_allow_html=True)

# Function to display password strength
def password_strength(password):
    result = zxcvbn(password)
    score = result['score']  # A score between 0 (weakest) and 4 (strongest)
    
    if score == 0:
        return 'Weak', 'bg-red-500'
    elif score == 1:
        return 'Weak', 'bg-red-500'
    elif score == 2:
        return 'Medium', 'bg-yellow-500'
    elif score == 3:
        return 'Strong', 'bg-pink-400'  # Light pink color for stronger passwords
    else:
        return 'Very Strong', 'bg-pink-500'  # Darker pink for very strong passwords

def main():
    # Apply Tailwind CSS and set background color for the entire page
    st.markdown("""
    <style>
        body {
            background-color: #FEE2E2;  /* Very light pink background */
        }
        .stTextInput input {
            border-radius: 0.375rem;
            padding: 0.75rem;
            border: 1px solid #FEC8D8;  /* Light pink border */
            background-color: #FEE2E2;  /* Light pink background */
        }
        .stButton button {
            background-color: #F9A8D4;  /* Soft pink for buttons */
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 0.375rem;
        }
        .stMarkdown {
            color: #9C2A4E;  /* Darker pink for text */
        }
    </style>
    """, unsafe_allow_html=True)

    st.title('Password Strength Meter')

    # Create a text input field for password
    password = st.text_input("Enter your password", type="password", label_visibility="collapsed")

    # Create a submit button
    if password:
        # Calculate the password strength
        strength, strength_class = password_strength(password)

        # Display password strength rating with light pink text
        st.markdown(f"<h3 class='text-2xl font-semibold mb-2 text-pink-500'>{strength}</h3>", unsafe_allow_html=True)

        # Display a strength bar using Tailwind CSS classes with pink shades
        st.markdown(f'<div class="w-full h-2 rounded-md {strength_class}"></div>', unsafe_allow_html=True)

        # Provide additional feedback and suggestions in light pink
        feedback = zxcvbn(password)['feedback']['suggestions']
        if feedback:
            st.markdown("<ul class='list-disc pl-5 space-y-2'>", unsafe_allow_html=True)
            for suggestion in feedback:
                st.markdown(f"<li class='text-sm text-gray-700'>{suggestion}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
