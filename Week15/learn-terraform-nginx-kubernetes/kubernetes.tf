terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_deployment" "nginx" {
  metadata {
    name = "scalable-nginx-example"
    labels = {
      App = "ScalableNginxExample"
    }
  }

  spec {
    replicas = 2
    selector {
      match_labels = {
        App = "ScalableNginxExample"
      }
    }
    template {
      metadata {
        labels = {
          App = "ScalableNginxExample"
        }
      }
      spec {
        container {
          image = "nginx:latest"
          name  = "example"

          port {
            container_port = 80
          }

          resources {
            limits = {
              cpu    = "128Mi"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "512Mi"
            }
          }
        }
      }
    }
  }
}
