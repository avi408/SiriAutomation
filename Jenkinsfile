pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out SiriAutomation from GitHub...'
                checkout scm
            }
        }

        stage('Environment Check') {
            steps {
                sh '''
                    echo "======================================"
                    echo "Environment Information"
                    echo "======================================"

                    echo "Python:"
                    /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 --version

                    echo "Git:"
                    git --version

                    echo "Node:"
                    node --version || true

                    echo "npm:"
                    npm --version || true

                    echo "Appium:"
                    appium --version || true
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "======================================"
                    echo "Creating Python virtual environment"
                    echo "======================================"

                    PYTHON=/Library/Frameworks/Python.framework/Versions/3.14/bin/python3

                    $PYTHON -m venv .venv

                    source .venv/bin/activate

                    echo "Python version:"
                    python --version

                    echo "Upgrading pip..."
                    pip install --upgrade pip

                    echo "Installing project dependencies..."
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "======================================"
                    echo "Running Behave Tests"
                    echo "======================================"

                    source .venv/bin/activate

                    behave
                '''
            }
        }
    }

    post {

        always {
            echo 'Test execution completed.'
        }

        success {
            echo 'SiriAutomation pipeline PASSED.'
        }

        failure {
            echo 'SiriAutomation pipeline FAILED.'
        }
    }
}
