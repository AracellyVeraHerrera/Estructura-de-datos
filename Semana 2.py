using System;

namespace FigurasGeometricas
{
    // Clase que representa un Círculo
    public class Circulo
    {
        private double radio; // Encapsula el radio del círculo

        // Constructor para inicializar el radio
        public Circulo(double radio)
        {
            if (radio <= 0)
            {
                throw new ArgumentException("El radio debe ser mayor a cero.");
            }
            this.radio = radio;
        }

        // Método para calcular el área del círculo
        public double CalcularArea()
        {
            // Fórmula: π * radio^2
            return Math.PI * Math.Pow(radio, 2);
        }

        // Método para calcular el perímetro del círculo
        public double CalcularPerimetro()
        {
            // Fórmula: 2 * π * radio
            return 2 * Math.PI * radio;
        }
    }

    // Clase que representa un Rectángulo
    public class Rectangulo
    {
        private double largo; // Encapsula el largo del rectángulo
        private double ancho; // Encapsula el ancho del rectángulo

        // Constructor para inicializar el largo y el ancho
        public Rectangulo(double largo, double ancho)
        {
            if (largo <= 0 || ancho <= 0)
            {
                throw new ArgumentException("El largo y el ancho deben ser mayores a cero.");
            }
            this.largo = largo;
            this.ancho = ancho;
        }

        // Método para calcular el área del rectángulo
        public double CalcularArea()
        {
            // Fórmula: largo * ancho
            return largo * ancho;
        }

        // Método para calcular el perímetro del rectángulo
        public double CalcularPerimetro()
        {
            // Fórmula: 2 * (largo + ancho)
            return 2 * (largo + ancho);
        }
    }

    // Clase principal para ejecutar el programa
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Ejemplo de uso de la clase Circulo
                Circulo circulo = new Circulo(5); // Radio = 5
                Console.WriteLine("Círculo:");
                Console.WriteLine($"Área: {circulo.CalcularArea():F2}");
                Console.WriteLine($"Perímetro: {circulo.CalcularPerimetro():F2}");

                // Ejemplo de uso de la clase Rectangulo
                Rectangulo rectangulo = new Rectangulo(10, 4); // Largo = 10, Ancho = 4
                Console.WriteLine("\nRectángulo:");
                Console.WriteLine($"Área: {rectangulo.CalcularArea():F2}");
                Console.WriteLine($"Perímetro: {rectangulo.CalcularPerimetro():F2}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
