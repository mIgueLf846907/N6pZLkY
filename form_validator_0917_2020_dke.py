# 代码生成时间: 2025-09-17 20:20:00
import gradio as gr
def validate_form(data):
    """
    Validate form data.
    Args:
        data (dict): A dictionary containing form fields and their values.
    Returns:
        dict: A dictionary containing validation results.
    """
    errors = {}
    # Validate 'email' field
    if not data.get('email') or '@' not in data['email']:
        errors['email'] = 'Invalid email address'
    
    # Validate 'age' field
    try:
        age = int(data.get('age', 0))
    except ValueError:
        errors['age'] = 'Age must be a number'
    else:
        if age < 0 or age > 120:
            errors['age'] = 'Age must be between 0 and 120'
    
    # Return validation results
    return {'errors': errors}

def main():
    """
    Main function to create and run the Gradio interface.
    """
    # Create a Gradio interface
    with gr.Blocks() as demo:
        gr.Markdown("# Form Data Validator")
        form = gr.FormItem()
        form.add_field(
            gr.Textbox(label="Email"), "email"
        )
        form.add_field(
            gr.Number(label="Age", value=25), "age"
        )
        submit = gr.Button("Submit")
        output = gr.Markdown()
        output_label = gr.Label("Validation Results")
        
        # Validate form data and display results
        def run_form_validator(data):
            if validate_form(data)['errors']:
                return f"Validation errors: {validate_form(data)['errors']}"
            else:
                return "All fields are valid!"
        
        submit.click(run_form_validator, inputs=form, outputs=output)
        
        form, output_label, output
        
    demo.launch()

if __name__ == "__main__":
    main()