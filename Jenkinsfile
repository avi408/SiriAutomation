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
                    PYTHON=/Library/Frameworks/Python.framework/Versions/3.14/bin/python3

                    echo "Creating virtual environment..."
                    $PYTHON -m venv .venv

                    source .venv/bin/activate

                    echo "Python:"
                    python --version

                    echo "Installing dependencies..."
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
    steps {
        sh '''
            source .venv/bin/activate

            mkdir -p reports

            behave \
                -f pretty \
                -f json \
                -o reports/behave-report.json
        '''
    }
}

    post {

    always {
        echo 'Test execution completed.'

        archiveArtifacts(
            artifacts: 'reports/**',
            allowEmptyArchive: true
        )
    }

    success {
        echo 'SiriAutomation pipeline PASSED.'
    }

    failure {
        echo 'SiriAutomation pipeline FAILED.'
    }
}
