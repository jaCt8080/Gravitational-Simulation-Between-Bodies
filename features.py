import pygame
import math
class Body:
  def __init__(self,color,radius,x_pos,y_pos,x_vel,y_vel,mass):
    self.color = color
    self.radius = radius
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.x_vel = x_vel
    self.y_vel = y_vel
    self.mass = mass
    self.x_acc =0 
    self.y_acc =0

  def movement(self,WIDTH,HEIGHT):
    self.x_pos+=self.x_vel
    self.y_pos+=self.y_vel

    if self.x_pos<self.radius and self.x_vel<0:
      self.x_vel*=-1
    elif self.x_pos>WIDTH-self.radius and self.x_vel>0:
      self.x_vel*=-1
    if self.y_pos<self.radius and self.y_vel<0:
      self.y_vel*=-1
    elif self.y_pos>HEIGHT-self.radius and self.y_vel>0:
      self.y_vel*=-1

  def gravity(self,other,G=1): # value of G need to change accod to simulation 
    Dx= other.x_pos-self.x_pos
    Dy= other.y_pos-self.y_pos
    R = math.hypot(Dx,Dy)
    if R>5:
      nx=Dx/R
      ny=Dy/R

      g_self = G*self.mass/(R**2)
      g_other = G*other.mass/(R**2)

      self.x_vel+=g_self*nx/200  # for now i am putting 200 division by try and error,need to be change
      self.y_vel+=g_self*ny/200
      other.x_vel-=g_other*nx/200
      other.y_vel-=g_other*ny/200

  def collision(self,other):
    Dx= other.x_pos-self.x_pos
    Dy= other.y_pos-self.y_pos
    D = math.hypot(Dx,Dy)
    m_d= self.radius+other.radius
    if D<m_d and D>0:
      nx=Dx/D
      ny=Dy/D
      total_mass = self.mass+other.mass
      overlap=m_d-D
      self.x_pos-=nx*overlap*(other.mass/total_mass)
      self.y_pos-=ny*overlap*(other.mass/total_mass)
      other.x_pos+=nx*overlap*(self.mass/total_mass)
      other.y_pos+=ny*overlap*(self.mass/total_mass)

      rel_x=self.x_vel-other.x_vel
      rel_y=self.y_vel-other.y_vel
      v_n=rel_x*nx + rel_y*ny
      if v_n>0:
        e=1.0
        k=((1+e)*v_n)/total_mass  # k is impulse
        self.x_vel -=nx*k*other.mass
        self.y_vel -=ny*k*other.mass 
        other.x_vel +=nx*k*self.mass
        other.y_vel +=ny*k*self.mass

  def visual(self,screen):
    pygame.draw.circle(screen,self.color,(int(self.x_pos),int(self.y_pos)),self.radius,width=0)
