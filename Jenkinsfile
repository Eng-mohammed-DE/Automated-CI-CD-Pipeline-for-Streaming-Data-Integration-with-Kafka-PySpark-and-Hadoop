pipeline {
    agent any  // This will use the default agent

    environment {
        // Set the virtual environment path based on your system setup
        PYTHON_ENV = '/home/eng-mohammed/master_node/venv'  // Adjusted path to your virtual environment
        SPARK_HOME = '/usr/local/spark'  // Path to your Spark installation
        KAFKA_HOME = '/opt/kafka'  // Path to your Kafka installation
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Activating the virtual environment and installing dependencies
                    sh '''
                    source ${PYTHON_ENV}/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    sh '''
                    source ${PYTHON_ENV}/bin/activate
                    python producer.py
                    '''
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    sh '''
                    source ${PYTHON_ENV}/bin/activate
                    ${SPARK_HOME}/bin/spark-submit --master local[*] consumer.py
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    echo 'Cleaning up resources...'
                    // Add any cleanup steps you need here
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline ran successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
