# Landing_Page/models.py

from django.db import models

class ContactSubmission(models.Model):
    """
    Modelo para armazenar as submissões do formulário de contato da landing page.
    """
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Mensagem")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Submissão")

    class Meta:
        verbose_name = "Submissão de Contato"
        verbose_name_plural = "Submissões de Contato"
        ordering = ['-submitted_at'] # Ordena por data de submissão decrescente

    def __str__(self):
        """
        Retorna uma representação em string do objeto.
        """
        return f"Contato de {self.name} ({self.email})"
