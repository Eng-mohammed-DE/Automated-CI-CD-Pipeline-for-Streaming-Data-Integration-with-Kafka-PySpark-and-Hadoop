pipeline {
    agent any
    environment {
        VENV_PATH = '/home/eng-mohammed/myenv'  // Use a path with proper permissions
        SPARK_HOME = '/usr/local/spark'
        KAFKA_HOME = '/opt/kafka'
    }

    stages {
        stage('Set Up Virtualenv') {
            steps {
                sh '''
                python3.11 -m venv ${VENV_PATH}  # Create the virtual environment
                source ${VENV_PATH}/bin/activate   # Activate the virtual environment
                pip install --upgrade pip         # Upgrade pip
                pip install -r requirements.txt   # Install dependencies
                '''
            }
        }
        // Other stages...
    }

    post {
        success {
            echo '✅ Pipeline ran successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
