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
                sh '''
                python3 -m venv ${VENV_PATH}
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
