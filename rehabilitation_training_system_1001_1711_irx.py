# 代码生成时间: 2025-10-01 17:11:53
import gradio as gr
def get_training_program(age, gender, injury_type):
    """
    Returns a rehabilitation training program based on the user's age, gender, and injury type.
    
    Parameters:
    age (int): The age of the user.
    gender (str): The gender of the user ('male' or 'female').
    injury_type (str): The type of injury the user has sustained.
    
    Returns:
    str: A description of the rehabilitation training program.
    """
    if not (age >= 0 and age < 100):
        raise ValueError("Age must be between 0 and 99")
    if gender not in ['male', 'female']:
        raise ValueError("Gender must be 'male' or 'female'")
    if injury_type not in ['knee', 'shoulder', 'back', 'wrist']:
        raise ValueError("Invalid injury type")

    # Define the rehabilitation training program based on the input parameters
    training_program = {
        'knee': 'Knee injury rehabilitation program',
        'shoulder': 'Shoulder injury rehabilitation program',
        'back': 'Back injury rehabilitation program',
        'wrist': 'Wrist injury rehabilitation program'
    }[(age // 10) * 100 + injury_type]
    return f"{training_program} suitable for {gender} aged {age}."

def main():
    """
    Creates a Gradio interface for the rehabilitation training system.
    """
    # Define the Gradio interface
    demo = gr.Interface(
        fn=get_training_program,
        inputs=["number", "radio", "radio"],
        outputs="text",
        title="Rehabilitation Training System",
        description="Select the age, gender, and injury type to generate a rehabilitation training program."
    )
    demo.launch()

if __name__ == "__main__":
    main()