from fastapi import APIRouter, HTTPException, status,Response
from typing import Optional, Dict, List, Any
from utils.models import Message, messages
import uvicorn
router = APIRouter()



@router.get('/api/v1/affirmations',summary='GET positive affirmations',
            description='GET all positive affirmations',response_model=List[Message])
async def get_cursos():
    return messages


@router.get('/api/v1/affirmations/{id}',summary='GET positive affirmations by ID',
            description='GET positive affirmations informin a ID',response_model=Message)
async def get_byid(id: int):
    try:
        message = messages[id]
        
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Tag not found.')

    return message

@router.post('/api/v1/affirmations', status_code= status.HTTP_201_CREATED, 
        summary='POST affirmation', description='POST positive affirmation', response_model=Message)
async def post_curso(msg: Message):
    next_id: int =  len(messages) + 1
    msg.id = next_id
    messages.append(msg)
        
    return msg


@router.put('/api/v1/affirmations/{msg_id}',summary='UPDATE by ID',
            description='UPDATE a positive affirmation by ID', response_model=Message)
async def put_curso(msg_id: int, msg: Message):
    #if msg_id in messages:
    if msg_id < len(messages):
        messages[msg_id] = msg
        

        return msg
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=F'Affirmartion {msg_id} not found.')
    
@router.delete('/api/v1/affirmations/{msg_id}',summary='DELETE by ID',
            description='DELETE a positive affirmation by ID', response_model=Message,response_description='Not a positive affirmation anymore :/')
async def delete_curso(msg_id: int):
    #if msg_id in messages:
    if msg_id < len(messages):
        del messages[msg_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=F'Affirmation {msg_id} not found.')
    
