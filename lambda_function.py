import json
import re

def lambda_handler(event, context):
    # Check if we have multiple test cases or a single email
    if 'testCases' in event:
        # Handle multiple test cases
        results = []
        for test_case in event['testCases']:
            email = test_case['email']
            name = test_case.get('name', f'Test for {email}')
            
            is_valid = validate_email(email)
            
            result = {
                'testName': name,
                'email': email,
                'isValid': is_valid,
                'status': 'PASS' if is_valid else 'FAIL',
                'message': 'Email address is valid' if is_valid else 'Email address is invalid'
            }
            results.append(result)
        
        # Summary
        total_tests = len(results)
        passed_tests = sum(1 for r in results if r['isValid'])
        failed_tests = total_tests - passed_tests
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'summary': {
                    'totalTests': total_tests,
                    'passed': passed_tests,
                    'failed': failed_tests
                },
                'results': results
            }, indent=2)
        }
    
    elif 'email' in event:
        # Handle single email (original functionality)
        email = event['email']
        if validate_email(email):
            return {
                'statusCode': 200,
                'body': json.dumps('Email address is valid')
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Email address is invalid')
            }
    
    else:
        # No valid input format
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input format. Expected either "email" or "testCases" field.')
        }

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
