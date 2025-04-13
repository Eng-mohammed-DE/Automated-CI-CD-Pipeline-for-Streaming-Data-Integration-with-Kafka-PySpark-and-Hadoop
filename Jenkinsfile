pipeline {
    agent any

    environment {
        PYTHON_ENV = '/home/eng-mohammed/master_node/venv'
        SPARK_HOME = '/usr/local/spark'
        KAFKA_HOME = '/opt/kafka'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    . ${PYTHON_ENV}/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    sh '''
                    . ${PYTHON_ENV}/bin/activate
                    python producer.py
                    '''
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    sh '''
                    . ${PYTHON_ENV}/bin/activate
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
