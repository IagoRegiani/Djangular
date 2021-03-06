from rest_framework import serializers

from .models import Administrador, Pessoa, Curso, Aula, Turma, ColaboradorTurma, PessoaAula

## PESSOA SERIALIZER #################
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

class GetPessoaSerializer(serializers.ModelDurationField):
    class Meta:
        model = Pessoa
        fields = ['Name', 'Email', 'Phone', 'UserType', 'StartDate', 'EndDate', 'Ativo',]

## ADMINISTRADOR SERIALIZER #################
class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

## CURSO SERIALIZER
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

## TURMA SERIALIZER #################
class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class GetTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
        depth = 1

## AULA SERIALIZER #################
class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'

class GetAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'
        depth = 1

## COLABORADOR-TURMA SERIALIZER #################
class ColaboradorTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColaboradorTurma
        fields = '__all__'

class ColaboradorOnlyTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColaboradorTurma
        fields = ['Turma',]
        depth = 2

class GetColaboradorTurmaSerializer(serializers.ModelSerializer):
    #prof_id = serializers.IntegerField(source="Colaborador.id")
    class Meta:
        model = Pessoa
        fields = '__all__'

## PESSOA-AULA SERIALIZER #################
class PessoaAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaAula
        fields = '__all__'
        print(fields)
        # fields = ['Contador', 'Aulas']

class GetPessoaAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaAula
        fields = '__all__'
        depth = 2
