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
                "~300 BCE": {
                    "figure": "Hero of Alexandria",
                    "contribution": "Discovered that light reflects at equal angles (angle of incidence = angle of reflection)",
                    "quote": "First hint that nature follows optimization principles",
                    "details": "Principle of least distance for reflection"
                },
                "~100 CE": {
                    "figure": "Ptolemy",
                    "contribution": "Studied refraction of light",
                    "quote": "Observed that light bends when passing through different media",
                    "details": "Laid groundwork for later optical principles"
                },
                "1621": {
                    "figure": "Willebrord Snellius",
                    "contribution": "Discovered Snell's law of refraction: n₁sin(θ₁) = n₂sin(θ₂)",
                    "quote": "Mathematical description of how light bends",
                    "details": "Another hint at optimization in nature"
                },
                "1687": {
                    "figure": "Isaac Newton",
                    "contribution": "Published Principia Mathematica, established three laws of motion",
                    "quote": "For every action, there is an equal and opposite reaction",
                    "details": "Created the foundation of classical mechanics",
                    "personality": "Notoriously secretive and competitive, feuded with Leibniz over calculus",
                    "background": "English mathematician, physicist, and astronomer"
                },
                "1744": {
                    "figure": "Pierre-Louis Maupertuis", 
                    "contribution": "First formulated the principle of least action",
                    "quote": "Nature is thrifty in all its actions and chooses ways that are shortest or most economical",
                    "details": "Applied optimization principles to physics",
                    "philosophy": "Believed nature operates with maximum efficiency and elegance",
                    "background": "French mathematician and philosopher"
                },
                "1750s": {
                    "figure": "Leonhard Euler",
                    "contribution": "Developed the mathematical framework for variational calculus",
                    "quote": "Euler-Lagrange equation: the mathematical heart of the action principle",
                    "details": "Applied optimization principles to many areas of mathematics and physics"
                },
                "1788": {
                    "figure": "Joseph-Louis Lagrange",
                    "contribution": "Developed Lagrangian mechanics based on action principle",
                    "quote": "The equations of motion follow from a single principle",
                    "details": "Systematic development of Lagrangian mechanics",
                    "innovation": "Transformed mechanics from force-based to energy-based",
                    "background": "Italian-French mathematician and astronomer"
                },
                "1833": {
                    "figure": "William Rowan Hamilton",
                    "contribution": "Formulated Hamiltonian mechanics and principle of stationary action",
                    "quote": "The true equations of dynamics are the Euler equations of the calculus of variations",
                    "details": "Phase space formulation: positions and momenta as independent variables",
                    "personality": "Child prodigy who knew 13 languages by age 13",
                    "background": "Irish mathematician, physicist, and astronomer"
                },
                "1860s": {
                    "figure": "James Clerk Maxwell",
                    "contribution": "Electromagnetic field theory",
                    "quote": "Showed how action principles apply to fields, not just particles",
                    "details": "Maxwell's equations from variational principles"
                },
                "1915": {
                    "figure": "Albert Einstein",
                    "contribution": "General relativity based on Einstein-Hilbert action",
                    "quote": "The most incomprehensible thing about the universe is that it is comprehensible",
                    "details": "Showed that spacetime itself follows variational principles"
                },
                "1948": {
                    "figure": "Richard Feynman",
                    "contribution": "Path integral formulation connecting action to quantum mechanics",
                    "quote": "Nature uses only the longest threads to weave her patterns",
                    "details": "Sum over histories approach",
                    "personality": "Known for curiosity, humor, and unconventional approach",
                    "background": "American theoretical physicist"
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
            ],
            'common_misconceptions': [
                "Normal force and weight are action-reaction pairs (they're not - both act on same object)",
                "Heavier objects fall faster in vacuum (they don't - all objects fall at same rate)",
                "Force is needed to maintain constant velocity (it's not - only to change velocity)",
                "Action-reaction forces cancel each other out (they don't - they act on different objects)"
            ],
            'institutions': [
                "Cambridge University: Newton's home institution",
                "École Polytechnique: Where Lagrange taught", 
                "Princeton University: Einstein's later career, Feynman's education",
                "Caltech: Feynman's career, modern physics research",
                "CERN: Modern particle physics and field theory"
            ],
            'practice_problems': [
                "Derive Newton's second law from the principle of least action for a simple harmonic oscillator",
                "Compare the Newtonian and Lagrangian approaches to solving a pendulum problem",
                "Explain how the action principle leads to conservation laws via Noether's theorem",
                "Apply the principle of least action to electromagnetic field theory",
                "Analyze the connection between classical action and quantum path integrals"
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
