import time
import os

class AnswerChecker:
    """
    This is an answer checker that simplifies the checking of test cases with timing feedback.
    """
    def __init__(self, eval_func, num_inputs):
        self.eval_func = eval_func
        self.num_inputs = num_inputs
        self.test_cases = []
        
        # Check for test_inputs and test_outputs files and load them if they exist
        if os.path.exists("test_inputs") and os.path.exists("test_outputs"):
            # Load inputs
            with open("test_inputs", "r") as f_in:
                input_lines = [line.strip() for line in f_in if line.strip()]
            
            # Load outputs
            with open("test_outputs", "r") as f_out:
                output_lines = [int(line.strip()) for line in f_out if line.strip()]
            
            # Group inputs and match them with outputs
            for i in range(0, len(input_lines), num_inputs):
                inputs = [eval(input_lines[j]) for j in range(i, i + num_inputs)]
                inputs_dict = {f"arg{j}": inputs[j] for j in range(num_inputs)}
                
                # Ensure we have a corresponding output
                output_index = i // num_inputs
                if output_index < len(output_lines):
                    correct_output = output_lines[output_index]
                    self.test_cases.append((inputs_dict, correct_output))
                else:
                    print(f"Warning: No matching output for input group starting at line {i+1}")

        else:
            print("Both test_inputs and test_outputs files must be present in the current directory.")

    def check_all(self, time_it=False):
        """
        Runs all test cases and checks the output.
        """
        for idx, (inputs, correct_output) in enumerate(self.test_cases, start=1):
            print(f"Running test case {idx}:")
            self.check(inputs, correct_output, time_it)

    def check(self, inputs, correct_output, time_it=False):
        """
        Runs a single test case and checks the output.
        """
        start = time.time()
        result = self.eval_func(**inputs)
        end = time.time()
        assert type(result) == int, "Output type is not int"
        
        if result == correct_output:
            if time_it:
                print(f"Correct solution computed in {round(end - start, 3)} seconds.")
        else:
            print(f"Wrong: {result} not equal to correct answer {correct_output}")
            exit(1)
