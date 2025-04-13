pipeline {
    agent any

    environment {
        VENV_PATH = '.venv'
        SPARK_HOME = '/usr/local/spark'
        KAFKA_HOME = '/opt/kafka'
        PYTHON_VERSION = 'python3.11'  // Ensure using the correct Python version
    }

    stages {
        stage('Check Python Version and Venv Dependencies') {
            steps {
                script {
                    echo '🔍 Verifying Python version and venv dependencies...'
                    sh '''
                        # Check if Python 3.11 is available
                        if ! ${PYTHON_VERSION} --version > /dev/null 2>&1; then
                            echo "❌ ${PYTHON_VERSION} is not installed!"
                            exit 1
                        else
                            echo "✅ Using ${PYTHON_VERSION}"
                        fi
                        
                        # Check if python3.11-venv is available
                        if ! ${PYTHON_VERSION} -m venv --help > /dev/null 2>&1; then
                            echo "❌ python3.11-venv is not available!"
                            echo "💡 Run: sudo apt install python3.11-venv"
                            exit 1
                        else
                            echo "✅ python3.11-venv is available."
                        fi
                    '''
                }
            }
        }

        stage('Set Up Virtualenv') {
            steps {
                script {
                    echo 'Creating and activating virtual environment...'
                    sh '''
                    # Create virtual environment
                    ${PYTHON_VERSION} -m venv ${VENV_PATH}
                    
                    # Activate virtual environment
                    . ${VENV_PATH}/bin/activate
                    
                    # Upgrade pip and install dependencies
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    echo 'Running Kafka Producer...'
                    sh '''
                    . ${VENV_PATH}/bin/activate
                    python producer.py
                    '''
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    echo 'Running Spark Consumer...'
                    sh '''
                    . ${VENV_PATH}/bin/activate
                    ${SPARK_HOME}/bin/spark-submit --master local[*] consumer.py
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                echo 'Cleaning up resources...'
            }
        }
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
