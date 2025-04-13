pipeline {
    agent any

    environment {
        VENV_PATH = '.venv'  // Virtual environment path
        SPARK_HOME = '/usr/local/spark'  // Spark installation path
        KAFKA_HOME = '/opt/kafka'  // Kafka installation path
    }

    stages {
        stage('Check Venv Dependencies') {
            steps {
                script {
                    echo '🔍 Verifying that python3.11-venv is installed...'
                    sh '''
                        if ! python3 -m venv --help > /dev/null 2>&1; then
                            echo "❌ python3.11-venv is not installed!"
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
                    python3.11 -m venv ${VENV_PATH}  # Create virtual environment
                    . ${VENV_PATH}/bin/activate  # Activate virtual environment
                    pip install --upgrade pip  # Upgrade pip to the latest version
                    pip install -r requirements.txt  # Install dependencies
                    '''
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    echo 'Running Kafka Producer...'
                    sh '''
                    . ${VENV_PATH}/bin/activate  # Activate virtual environment
                    python producer.py  # Run Kafka producer
                    '''
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    echo 'Running Spark Consumer...'
                    sh '''
                    . ${VENV_PATH}/bin/activate  # Activate virtual environment
                    ${SPARK_HOME}/bin/spark-submit --master local[*] consumer.py  # Run Spark consumer
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
