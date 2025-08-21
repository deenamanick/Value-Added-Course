terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "quiz_app" {
  name = "quiz-app:latest"
  build {
    context    = "/home/vagrant/terraform-docker/k8s-quiz"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "quiz_app" {
  name  = "quiz_app"
  image = docker_image.quiz_app.image_id
  ports {
    internal = 5000
    external = 5000
  }
}
