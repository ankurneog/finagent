# llm/llm_wrapper.py
from typing import Optional, List, Literal, Dict
import asyncio

# For llama.cpp
from llama_cpp import Llama

# For Ollama
try:
    import ollama
except ImportError:
    ollama = None  # Ollama is optional, handle import error gracefully

class LLMWrapper:
    def __init__(
        self,
        backend: Literal["ollama", "llama.cpp"],
        model: str,
        llama_config: Optional[Dict] = None,
    ):
        self.backend = backend
        self.model = model

        if backend == "llama.cpp":
            self.llm = Llama(
                model_path=model,
                n_ctx=llama_config.get("n_ctx", 4096),
                n_threads=llama_config.get("n_threads", 8),
                n_gpu_layers=llama_config.get("n_gpu_layers", 32),
            )
        elif backend == "ollama":
            if ollama is None:
                raise ImportError("Ollama is not installed.")
        else:
            raise ValueError("Unsupported backend. Choose 'ollama' or 'llama.cpp'.")

    async def chat(self, prompt: str) -> str:
        if self.backend == "ollama":
            return self._chat_ollama(prompt)
        elif self.backend == "llama.cpp":
            return await self._chat_llama_cpp(prompt)

    def _chat_ollama(self, prompt: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]

    async def _chat_llama_cpp(self, prompt: str) -> str:
        response = await asyncio.to_thread(
            self.llm,
            prompt=prompt,
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
            stop=["</s>"]
        )
        return response["choices"][0]["text"].strip()
