import openai

class Grader:
    def __init__(self):
        self.b_parameters = ['Professionalism', 'Interpersonal skills', 'Attitude', 'Experience']
        self.t_parameters = ['Problem-solving ability', 'Accuracy', 'Reasoning']

    def build_message(self, transcript, type):
        if (type == 'b' or type == 'B'):
            message=[
                {'role':'system', 'content':
                    f"You are given an interview transcript. Grade the applicant"
                    "according to these parameters: {', '.join(self.b_parameters)}"
                    "Each parameter can be graded out of 5. Output ex:"
                    "Professionalism: 5, Interpersonal skills: 4, etc."
                    "Then the sum is the total score"
                    "Include the type of interview in the intro"
                },
                {'role':'user', 
                    'content':f"Grade this transcript: {transcript}"
                }
            ]

        elif (type == 't' or type == 'T'):
            message=[
                {'role':'system', 'content':
                    "You are given an interview transcript. Grade the applicant"
                    "according to these parameters: {', '.join(self.t_parameters)}"
                    "Each parameter can be graded out of 5. Output ex:"
                    "Accuracy: 5, Reasoning: 4, etc."
                    "Then the sum is the total score."
                    "Include the type of interview in the intro"
                },
                {'role':'user', 
                    'content':f"Grade this transcript: {transcript}"
                }
            ]

        else:
            message=[
                {'role':'system', 'content':
                    "You are given an interview transcript. Grade the applicant"
                    "according to these parameters: {', '.join(b_parameters)}"
                    "Each parameter can be graded out of 5. Output ex:"
                    "Accuracy: 5, Reasoning: 4, etc."
                    "Then the sum is the total score"
                    "Include the type of interview in the intro"
                },
                {'role':'user', 
                    'content':f"Grade this transcript: {transcript}"
                }
            ]

        return message

    def grade_interview(self, transcript, type):
        message=self.build_message(transcript, type)
        try:
            print('Loading...')
            response = openai.chat.completions.create(
                model='gpt-4o-mini',
                messages=message
            )
            grade = response.choices[0].message.content.strip()

            return grade

        except Exception as e:
            raise e