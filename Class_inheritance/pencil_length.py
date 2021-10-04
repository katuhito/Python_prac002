#組み込み型のサブクラスを作成
class Length(float):
    def to_cm(self):
        return super().__str__() + 'cm'

#インスタンス化
pencil_length = Length(16)
print(pencil_length.to_cm())