# Latent Diffusion Models
The latent diffusion models (LDMs) is a simple and efficient way to siginificantly improve both the training and sampling efficiency of denoising diffusion models without degrading their quality. 

## Brief Introduction


## Latent Diffusion Model
1. Diffusion Models are designed to learn a data distribution $p(x)$ by gradually denoising a normally distributed variable, which corresponds to learning the reverse process of a fixed Markov Chain of legth $T$. 
2. Generative Modeling of Latent Representations
3. Conditioning Mechanisms \
    Diffusion models are capable of modeling conditional distributions of the form $p(z|y)$. This can be implemented with a conditional denoising autoenoder $\epsilon_\theta(z_t, t, y)$ amd paves the way to controlling the synthesis process through inputs $y$ such as text, semantic maps or other image-to-image translation tasks. 



# Code Notes
1. Torch does not support `torch._six` anymore, so remove `from torch._six import string_classes`.
2. Replace `string_classes` with `str`. 
