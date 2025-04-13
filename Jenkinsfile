pipeline {
    agent any
    environment {
        VENV_PATH = '.venv'  
        SPARK_HOME = '/usr/local/spark'
        KAFKA_HOME = '/opt/kafka'
    }

    stages {
        stage('Set Up Virtualenv') {
            steps {
                script {
                    echo '🔧 Setting up virtual environment...'
                    sh '''
                        python3.11 -m venv ${VENV_PATH}  # Create the virtual environment
                        source ${VENV_PATH}/bin/activate  # Activate the virtual environment
                        pip install --upgrade pip         # Upgrade pip
                        pip install -r requirements.txt   # Install dependencies
                    '''
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    echo '🚀 Running Kafka producer...'
                    sh '''
                        source ${VENV_PATH}/bin/activate  # Activate virtual environment
                        python producer.py                 # Run the producer
                    '''
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    echo '🚀 Running Spark consumer...'
                    sh '''
                        source ${VENV_PATH}/bin/activate  # Activate virtual environment
                        ${SPARK_HOME}/bin/spark-submit --master local[*] consumer.py  # Run the Spark consumer
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                echo '🧹 Cleaning up resources...'
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
