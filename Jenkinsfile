pipeline {
    agent {
        node {
            label 'Muscle-Agent'
        }
    }

    options {
        timeout(time: 1, unit: 'HOURS')
        retry(1)
    }

    environment {
        POETRY_HOME = "${WORKSPACE}/.poetry"
        PATH = "${POETRY_HOME}/bin:${PATH}"
    }

    stages {

        stage('Check Environment') {
            steps {
                echo "Checking Python and Poetry installation"
                sh '''
                    python3 --version
                    poetry --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies"
                sh '''
                    poetry install --no-interaction --no-root
                '''
            }
            post {
                success {
                    echo "Dependencies installed successfully"
                }
                failure {
                    echo "Dependency installation failed"
                    sh 'tail -n 10 install_log.txt || true'
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests and generating HTML report"
                sh '''
                    mkdir -p reports
                    poetry run pytest --maxfail=1 --disable-warnings \
                        --html=reports/test_report.html --self-contained-html
                '''
            }
        }

        stage('Build Project') {
            steps {
                echo "Building project with Poetry"
                sh '''
                    mkdir -p build_output
                    poetry build -f wheel -f sdist
                    cp dist/* build_output/
                '''
            }
        }
    }

    post {
        always {
            echo "Archiving artifacts..."
            archiveArtifacts artifacts: 'build_output/*, reports/test_report.html', fingerprint: true
        }
    }
}
