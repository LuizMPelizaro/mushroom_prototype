class RegexMush:
    def __init__(self, dict_mush: dict):
        self.__dict_mush = dict_mush

    @property
    def dict_mush(self):
        return self.__dict_mush

    def regex(self) -> None:
        for key in self.dict_mush:
            if key == 'cap-shape':
                if self.dict_mush[key] == ['Sino']:
                    self.dict_mush[key] = ['b']
                elif self.dict_mush[key] == ['Cone']:
                    self.dict_mush[key] = ['c']
                elif self.dict_mush[key] == ['Convexo']:
                    self.dict_mush[key] = ['x']
                elif self.dict_mush[key] == ['Plano']:
                    self.dict_mush[key] = ['f']
                elif self.dict_mush[key] == ['Arredondada']:
                    self.dict_mush[key] = ['k']
                elif self.dict_mush[key] == ['Fundo']:
                    self.dict_mush[key] = ['s']
                else:
                    raise ValueError
            elif key == 'cap-surface':
                if self.dict_mush[key] == ['Fibroso']:
                    self.dict_mush[key] = ['f']
                elif self.dict_mush[key] == ['Sulcos']:
                    self.dict_mush[key] = ['g']
                elif self.dict_mush[key] == ['Escamoso']:
                    self.dict_mush[key] = ['y']
                elif self.dict_mush[key] == ['Liso']:
                    self.dict_mush[key] = ['s']
                else:
                    raise ValueError
            elif key == 'cap-color':
                if self.dict_mush[key] == ['Marrom']:
                    self.dict_mush[key] = ['n']
                elif self.dict_mush[key] == ['Bege']:
                    self.dict_mush[key] = ['b']
                elif self.dict_mush[key] == ['Canela']:
                    self.dict_mush[key] = ['c']
                elif self.dict_mush[key] == ['Cinza']:
                    self.dict_mush[key] = ['g']
                elif self.dict_mush[key] == ['Verde']:
                    self.dict_mush[key] = ['r']
                elif self.dict_mush[key] == ['Rosa']:
                    self.dict_mush[key] = ['p']
                elif self.dict_mush[key] == ['Roxo']:
                    self.dict_mush[key] = ['u']
                elif self.dict_mush[key] == ['Vermelho']:
                    self.dict_mush[key] = ['e']
                elif self.dict_mush[key] == ['Branco']:
                    self.dict_mush[key] = ['w']
                elif self.dict_mush[key] == ['Amarelo']:
                    self.dict_mush[key] = ['y']
                else:
                    raise ValueError
            elif key == 'bruises':
                if self.dict_mush[key] == ['Sim']:
                    self.dict_mush[key] = ['t']
                elif self.dict_mush[key] == ['Não']:
                    self.dict_mush[key] = ['f']
                else:
                    raise ValueError
            elif key == 'odor':
                if self.dict_mush[key] == ['Amêndoa']:
                    self.dict_mush[key] = ['a']
                elif self.dict_mush[key] == ['Anis']:
                    self.dict_mush[key] = ['l']
                elif self.dict_mush[key] == ['Creosote']:
                    self.dict_mush[key] = ['c']
                elif self.dict_mush[key] == ['Peixe']:
                    self.dict_mush[key] = ['y']
                elif self.dict_mush[key] == ['Fétido']:
                    self.dict_mush[key] = ['f']
                elif self.dict_mush[key] == ['Mofo']:
                    self.dict_mush[key] = ['m']
                elif self.dict_mush[key] == ['Nenhum']:
                    self.dict_mush[key] = ['n']
                elif self.dict_mush[key] == ['Pungente']:
                    self.dict_mush[key] = ['p']
                elif self.dict_mush[key] == ['Picante']:
                    self.dict_mush[key] = ['s']
                else:
                    raise ValueError
            elif key == 'gill-attachment':
                if self.dict_mush[key] == ['Anexado']:
                    self.dict_mush[key] = ['a']
                elif self.dict_mush[key] == ['Descendente']:
                    self.dict_mush[key] = ['d']
                elif self.dict_mush[key] == ['Livre']:
                    self.dict_mush[key] = ['f']
                elif self.dict_mush[key] == ['Entalhado']:
                    self.dict_mush[key] = ['n']
                else:
                    raise ValueError
            elif key == 'gill-spacing':
                if self.dict_mush[key] == ['Perto']:
                    self.dict_mush[key] = ['c']
                elif self.dict_mush[key] == ['Sobrecarregado']:
                    self.dict_mush[key] = ['w']
                elif self.dict_mush[key] == ['Afastadas']:
                    self.dict_mush[key] = ['d']
                else:
                    raise ValueError
            elif key == 'gill-size':
                if self.dict_mush[key] == ['Largo']:
                    self.dict_mush[key] = ['b']
                elif self.dict_mush[key] == ['Estreita']:
                    self.dict_mush[key] = ['n']
                else:
                    raise ValueError
            elif key == 'gill-color':
                if self.dict_mush[key] == ['Preto']:
                    self.dict_mush[key] = ['k']
                elif self.dict_mush[key] == ['Marrom']:
                    self.dict_mush[key] = ['n']
                elif self.dict_mush[key] == ['Bege']:
                    self.dict_mush[key] = ['b']
                elif self.dict_mush[key] == ['Chocolate']:
                    self.dict_mush[key] = ['h']
                elif self.dict_mush[key] == ['Cinza']:
                    self.dict_mush[key] = ['g']
                elif self.dict_mush[key] == ['Verde']:
                    self.dict_mush[key] = ['r']
                elif self.dict_mush[key] == ['Laranja']:
                    self.dict_mush[key] = ['o']
                elif self.dict_mush[key] == ['Rosa']:
                    self.dict_mush[key] = ['p']
                elif self.dict_mush[key] == ['Roxa']:
                    self.dict_mush[key] = ['u']
                elif self.dict_mush[key] == ['Vermelho']:
                    self.dict_mush[key] = ['e']
                elif self.dict_mush[key] == ['Branco']:
                    self.dict_mush[key] = ['w']
                elif self.dict_mush[key] == ['Amarelo']:
                    self.dict_mush[key] = ['y']
                else:
                    raise ValueError
            elif key == 'stalk-shape':
                if self.dict_mush[key] == ['Ampliação']:
                    self.dict_mush[key] = ['e']
                elif self.dict_mush[key] == ['Afunilado']:
                    self.dict_mush[key] = ['t']
                else:
                    raise ValueError
            elif key == 'stalk-root':
                if self.dict_mush[key] == ['Bulboso']:
                    self.dict_mush[key] = ['b']
                elif self.dict_mush[key] == ['Clube']:
                    self.dict_mush[key] = ['c']
                elif self.dict_mush[key] == ['Copo']:
                    self.dict_mush[key] = ['u']
                elif self.dict_mush[key] == ['Uniforme']:
                    self.dict_mush[key] = ['e']
                elif self.dict_mush[key] == ['Rizomorfos']:
                    self.dict_mush[key] = ['z']
                elif self.dict_mush[key] == ['Enraizado']:
                    self.dict_mush[key] = ['r']
                elif self.dict_mush[key] == ['Faltante']:
                    self.dict_mush[key] = ['?']
                else:
                    raise ValueError
            elif key == 'stalk-surface-above-ring' or key == 'stalk-surface-below-ring':
                if self.dict_mush[key] == ['Fibroso']:
                    self.dict_mush[key] = ['f']
                elif self.dict_mush[key] == ['Escamoso']:
                    self.dict_mush[key] = ['y']
                elif self.dict_mush[key] == ['Sedoso']:
                    self.dict_mush[key] = ['k']
                elif self.dict_mush[key] == ['Liso']:
                    self.dict_mush[key] = ['s']
                else:
                    raise ValueError
            elif key == 'stalk-color-above-ring' or key == 'stalk-color-below-ring':
                if self.dict_mush[key] == ['Marrom']:
                    self.dict_mush[key] = ['n']
                elif self.dict_mush[key] == ['Bege']:
                    self.dict_mush[key] = ['b']
                elif self.dict_mush[key] == ['Canela']:
                    self.dict_mush[key] = ['c']
                elif self.dict_mush[key] == ['Cinza']:
                    self.dict_mush[key] = ['g']
                elif self.dict_mush[key] == ['Laranja']:
                    self.dict_mush[key] = ['o']
                elif self.dict_mush[key] == ['Rosa']:
                    self.dict_mush[key] = ['p']
                elif self.dict_mush[key] == ['Vermelho']:
                    self.dict_mush[key] = ['e']
                elif self.dict_mush[key] == ['Branco']:
                    self.dict_mush[key] = ['w']
                elif self.dict_mush[key] == ['Amarelo']:
                    self.dict_mush[key] = ['y']
                else:
                    raise ValueError
            elif key == 'veil-type':
                if self.dict_mush[key] == ['Parcial']:
                    self.dict_mush[key] = ['p']
                elif self.dict_mush[key] == ['Total']:
                    self.dict_mush[key] = ['u']
                else:
                    raise ValueError
            elif key == 'veil-color':
                if self.dict_mush[key] == ['Marrom']:
                    self.dict_mush[key] = ['n']
                elif self.dict_mush[key] == ['Laranja']:
                    self.dict_mush[key] = ['o']
                elif self.dict_mush[key] == ['Branco']:
                    self.dict_mush[key] = ['w']
                elif self.dict_mush[key] == ['Amarelo']:
                    self.dict_mush[key] = ['y']
                else:
                    raise ValueError
            elif key == 'ring-number':
                if self.dict_mush[key] == ['Nenhum']:
                    self.dict_mush[key] = ['n']
                elif self.dict_mush[key] == ['Um']:
                    self.dict_mush[key] = ['o']
                elif self.dict_mush[key] == ['Dois']:
                    self.dict_mush[key] = ['t']
                else:
                    raise ValueError
            elif key == 'ring-type':
                if self.dict_mush[key] == ['Teia']:
                    self.dict_mush[key] = ['c']
                elif self.dict_mush[key] == ['Evanescente']:
                    self.dict_mush[key] = ['e']
                elif self.dict_mush[key] == ['Vistoso']:
                    self.dict_mush[key] = ['f']
                elif self.dict_mush[key] == ['Grande']:
                    self.dict_mush[key] = ['l']
                elif self.dict_mush[key] == ['Nenhum']:
                    self.dict_mush[key] = ['n']
                elif self.dict_mush[key] == ['Pingente']:
                    self.dict_mush[key] = ['p']
                elif self.dict_mush[key] == ['Revestimento']:
                    self.dict_mush[key] = ['s']
                elif self.dict_mush[key] == ['Zona']:
                    self.dict_mush[key] = ['z']
                else:
                    raise ValueError
            elif key == 'spore-print-color':
                if self.dict_mush[key] == ['Preto']:
                    self.dict_mush[key] = ['k']
                elif self.dict_mush[key] == ['Marrom']:
                    self.dict_mush[key] = ['n']
                elif self.dict_mush[key] == ['Bege']:
                    self.dict_mush[key] = ['b']
                elif self.dict_mush[key] == ['Chocolate']:
                    self.dict_mush[key] = ['h']
                elif self.dict_mush[key] == ['Verde']:
                    self.dict_mush[key] = ['r']
                elif self.dict_mush[key] == ['Laranja']:
                    self.dict_mush[key] = ['o']
                elif self.dict_mush[key] == ['Roxo']:
                    self.dict_mush[key] = ['u']
                elif self.dict_mush[key] == ['Branco']:
                    self.dict_mush[key] = ['w']
                elif self.dict_mush[key] == ['Amarelo']:
                    self.dict_mush[key] = ['y']
                else:
                    raise ValueError
            elif key == 'population':
                if self.dict_mush[key] == ['Abundante']:
                    self.dict_mush[key] = ['a']
                elif self.dict_mush[key] == ['Agrupado']:
                    self.dict_mush[key] = ['c']
                elif self.dict_mush[key] == ['Numeroso']:
                    self.dict_mush[key] = ['n']
                elif self.dict_mush[key] == ['Disperso']:
                    self.dict_mush[key] = ['s']
                elif self.dict_mush[key] == ['Varios']:
                    self.dict_mush[key] = ['v']
                elif self.dict_mush[key] == ['Solitario']:
                    self.dict_mush[key] = ['y']
                else:
                    raise ValueError
            elif key == 'habitat':
                if self.dict_mush[key] == ['Grama']:
                    self.dict_mush[key] = ['g']
                elif self.dict_mush[key] == ['Folhas']:
                    self.dict_mush[key] = ['l']
                elif self.dict_mush[key] == ['Prados']:
                    self.dict_mush[key] = ['m']
                elif self.dict_mush[key] == ['Caminho']:
                    self.dict_mush[key] = ['p']
                elif self.dict_mush[key] == ['Urbano']:
                    self.dict_mush[key] = ['u']
                elif self.dict_mush[key] == ['Lixo']:
                    self.dict_mush[key] = ['w']
                elif self.dict_mush[key] == ['Bosques']:
                    self.dict_mush[key] = ['d']
                else:
                    raise ValueError
