from src.core.usecases.usecases import NoParams
from src.domain.usecases.get_posters_usecase import GetPostersUsecase

usecase = GetPostersUsecase()

result = usecase.call(input=NoParams())

print(result[0].url)
