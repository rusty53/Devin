class PhysicsKnowledge:
    """Domain-specific knowledge base for physics topics"""
    
    @staticmethod
    def get_topic_data(topic_name):
        topic_lower = topic_name.lower()
        
        if "law of action" in topic_lower or "action" in topic_lower:
            return PhysicsKnowledge._get_action_principle_data()
        elif "quantum" in topic_lower:
            return PhysicsKnowledge._get_quantum_mechanics_data()
        elif "machine learning" in topic_lower:
            return PhysicsKnowledge._get_machine_learning_data()
        elif "calculus" in topic_lower:
            return PhysicsKnowledge._get_calculus_data()
        else:
            return PhysicsKnowledge._get_generic_data(topic_name)
    
    @staticmethod
    def _get_action_principle_data():
        return {
            'mathematical_foundations': [
                "Action S = ∫ L dt, where L is the Lagrangian (T - V)",
                "T = kinetic energy, V = potential energy", 
                "Physical paths satisfy δS = 0 (variational principle)",
                "Euler-Lagrange equation: d/dt(∂L/∂q̇) - ∂L/∂q = 0"
            ],
            'key_concepts': [
                "Principle of Least Action - fundamental principle underlying all physics",
                "Newton's Laws of Motion - F = ma, inertia, action-reaction",
                "Lagrangian Mechanics - energy-based formulation",
                "Hamiltonian Formulation - phase space approach",
                "Path Integral Formulation - quantum mechanical extension"
            ],
            'historical_timeline': {
                "1687": {
                    "figure": "Isaac Newton",
                    "contribution": "Published Principia Mathematica, established three laws of motion",
                    "quote": "For every action, there is an equal and opposite reaction"
                },
                "1744": {
                    "figure": "Pierre-Louis Maupertuis", 
                    "contribution": "First formulated the principle of least action",
                    "quote": "Nature is thrifty in all its actions"
                },
                "1788": {
                    "figure": "Joseph-Louis Lagrange",
                    "contribution": "Developed Lagrangian mechanics based on action principle",
                    "quote": "The equations of motion follow from a single principle"
                },
                "1833": {
                    "figure": "William Rowan Hamilton",
                    "contribution": "Formulated Hamiltonian mechanics and principle of stationary action",
                    "quote": "The true equations of dynamics are the Euler equations of the calculus of variations"
                },
                "1915": {
                    "figure": "Albert Einstein",
                    "contribution": "General relativity based on Einstein-Hilbert action",
                    "quote": "The most incomprehensible thing about the universe is that it is comprehensible"
                },
                "1948": {
                    "figure": "Richard Feynman",
                    "contribution": "Path integral formulation connecting action to quantum mechanics",
                    "quote": "Nature uses only the longest threads to weave her patterns"
                }
            },
            'applications': [
                "Classical mechanics and orbital dynamics",
                "Quantum field theory and particle physics", 
                "General relativity and cosmology",
                "Engineering optimization and control systems",
                "Robotics and mechanical design"
            ],
            'learning_progression': [
                "Newton's laws and basic mechanics",
                "Energy conservation and work-energy theorem",
                "Calculus of variations and Euler-Lagrange equations",
                "Lagrangian mechanics and generalized coordinates",
                "Hamiltonian mechanics and phase space",
                "Quantum mechanics and path integrals"
            ]
        }
    
    @staticmethod
    def _get_quantum_mechanics_data():
        return {
            'mathematical_foundations': [
                "Schrödinger equation: iℏ ∂ψ/∂t = Ĥψ",
                "Wave function ψ contains all quantum information",
                "Born rule: |ψ|² gives probability density",
                "Uncertainty principle: ΔxΔp ≥ ℏ/2"
            ],
            'key_concepts': [
                "Wave-particle duality",
                "Quantum superposition and entanglement", 
                "Measurement and wave function collapse",
                "Quantum tunneling and interference"
            ],
            'historical_timeline': {
                "1900": {
                    "figure": "Max Planck",
                    "contribution": "Introduced quantum hypothesis for blackbody radiation",
                    "quote": "Energy is quantized in discrete packets"
                },
                "1905": {
                    "figure": "Albert Einstein", 
                    "contribution": "Explained photoelectric effect with light quanta",
                    "quote": "Light has a particle nature"
                },
                "1925": {
                    "figure": "Werner Heisenberg",
                    "contribution": "Developed matrix mechanics formulation",
                    "quote": "What we observe is not nature itself, but nature exposed to our method of questioning"
                }
            }
        }
    
    @staticmethod
    def _get_machine_learning_data():
        return {
            'mathematical_foundations': [
                "Gradient descent: θ = θ - α∇J(θ)",
                "Backpropagation algorithm for neural networks",
                "Loss functions: MSE, cross-entropy, etc.",
                "Regularization: L1, L2, dropout"
            ],
            'key_concepts': [
                "Supervised vs unsupervised learning",
                "Neural networks and deep learning",
                "Feature engineering and selection",
                "Overfitting and generalization"
            ],
            'historical_timeline': {
                "1943": {
                    "figure": "Warren McCulloch & Walter Pitts",
                    "contribution": "First mathematical model of artificial neuron",
                    "quote": "A logical calculus of ideas immanent in nervous activity"
                },
                "1957": {
                    "figure": "Frank Rosenblatt",
                    "contribution": "Invented the perceptron algorithm",
                    "quote": "The perceptron is capable of learning"
                }
            }
        }
    
    @staticmethod
    def _get_calculus_data():
        return {
            'mathematical_foundations': [
                "Derivative: f'(x) = lim[h→0] (f(x+h) - f(x))/h",
                "Integral: ∫f(x)dx represents area under curve",
                "Fundamental Theorem: d/dx ∫f(t)dt = f(x)",
                "Chain rule: (f∘g)'(x) = f'(g(x))·g'(x)"
            ],
            'key_concepts': [
                "Limits and continuity",
                "Differentiation and integration",
                "Applications to optimization",
                "Differential equations"
            ],
            'historical_timeline': {
                "1665": {
                    "figure": "Isaac Newton",
                    "contribution": "Developed method of fluxions (calculus)",
                    "quote": "Method of fluxions and infinite series"
                },
                "1684": {
                    "figure": "Gottfried Leibniz",
                    "contribution": "Published first paper on differential calculus",
                    "quote": "dx and dy notation for infinitesimals"
                }
            }
        }
    
    @staticmethod
    def _get_generic_data(topic_name):
        return {
            'mathematical_foundations': [
                f"Core mathematical principles underlying {topic_name}",
                "Fundamental equations and relationships",
                "Quantitative methods and analysis",
                "Mathematical modeling approaches"
            ],
            'key_concepts': [
                f"Fundamental principles of {topic_name}",
                "Theoretical frameworks and models",
                "Practical applications and implementations",
                "Current research directions"
            ],
            'historical_timeline': {
                "Ancient": {
                    "figure": "Early Pioneers",
                    "contribution": "Foundational observations and theories",
                    "quote": "The beginning of understanding"
                }
            }
        }
