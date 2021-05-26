from src.domain.usecases.get_posters_usecase import GetPostersUsecase

usecase = GetPostersUsecase()

result = usecase.call()

print(result)
