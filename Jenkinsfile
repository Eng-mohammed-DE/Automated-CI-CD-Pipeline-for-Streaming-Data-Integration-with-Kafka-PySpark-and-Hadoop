pipeline {
    agent any

    environment {
        VENV_PATH = '.venv'  // Virtual environment path
        SPARK_HOME = '/usr/local/spark'  // Spark installation path
        KAFKA_HOME = '/opt/kafka'  // Kafka installation path
    }

    stages {
        stage('Set Up Virtualenv') {
            steps {
                sh '''
                python3.11 -m venv ${VENV_PATH}  # Create the virtual environment
                . ${VENV_PATH}/bin/activate  # Activate the virtual environment
                pip install --upgrade pip  # Upgrade pip to the latest version
                pip install -r requirements.txt  # Install dependencies from requirements.txt
                '''
            }
        }

        stage('Run Kafka Producer') {
            steps {
                sh '''
                . ${VENV_PATH}/bin/activate  # Activate the virtual environment
                python producer.py  # Run Kafka producer
                '''
            }
        }

        stage('Run Spark Consumer') {
            steps {
                sh '''
                . ${VENV_PATH}/bin/activate  # Activate the virtual environment
                ${SPARK_HOME}/bin/spark-submit --master local[*] consumer.py  # Run Spark consumer
                '''
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
