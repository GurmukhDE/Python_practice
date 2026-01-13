from loguru import logger

l= [1,11,18,2,4,5,6,78,8]

logger.info(list(enumerate(l)))

logger.info(l.reverse())
logger.info(l)

logger.info(l.sort())
logger.info(l)

first, *middle, last = l
