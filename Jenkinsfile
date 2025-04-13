pipeline {
    agent any

    environment {
        VENV_PATH = '.venv'
        SPARK_HOME = '/usr/local/spark'
        KAFKA_HOME = '/opt/kafka'
        PYTHON_VERSION = '/usr/bin/python3.11'  // Full path to Python 3.11
    }

    stages {
        stage('Set Up Virtualenv') {
            steps {
                sh '''
                ${PYTHON_VERSION} -m venv ${VENV_PATH}
                . ${VENV_PATH}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Kafka Producer') {
            steps {
                sh '''
                . ${VENV_PATH}/bin/activate
                python producer.py
                '''
            }
        }

        stage('Run Spark Consumer') {
            steps {
                sh '''
                . ${VENV_PATH}/bin/activate
                ${SPARK_HOME}/bin/spark-submit --master local[*] consumer.py
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
