#!/usr/bin/env python3
"""Corrige seis errores de compilacion observados en NAIMSAURIA 26.2.
Ejecutar desde la raiz del repositorio: python3 fix_naimsauria_26_2.py
"""
from pathlib import Path

boss = Path('src/main/java/net/naimsauria/titanes/entity/NaimsaurPrimeEntity.java')
sigil = Path('src/main/java/net/naimsauria/titanes/item/PrimordialSigilItem.java')

def change(s, old, new):
    if old in s:
        if s.count(old) != 1:
            raise RuntimeError('Texto ambiguo: ' + old[:75])
        return s.replace(old, new)
    if new in s:
        return s
    raise RuntimeError('No se encontro texto esperado: ' + old[:75])

s = boss.read_text(encoding='utf-8')
s = change(s, 'import net.minecraft.core.particles.ParticleTypes;', 'import java.util.UUID;\nimport net.minecraft.core.particles.ParticleTypes;')
s = change(s, 'new ServerBossEvent(\n        Component.literal', 'new ServerBossEvent(\n        UUID.randomUUID(), Component.literal')
s = change(s, 'new AnimationController<>(this, "movement", 5, state ->', 'new AnimationController<>("movement", 5, state ->')
s = change(s, 'new AnimationController<>(this, "actions", 0, state ->', 'new AnimationController<>("actions", 0, state ->')
s = change(s, 'server.sendParticles(ParticleTypes.DRAGON_BREATH, aimedAt.x', 'server.sendParticles(ParticleTypes.REVERSE_PORTAL, aimedAt.x')
boss.write_text(s, encoding='utf-8')

s = sigil.read_text(encoding='utf-8')
s = change(s, '''        boss.moveTo(altar.getX() + 0.5, altar.getY(), altar.getZ() + 0.5,
                level.random.nextFloat() * 360, 0);''', '''        boss.setPos(altar.getX() + 0.5, altar.getY(), altar.getZ() + 0.5);
        boss.setYRot(level.getRandom().nextFloat() * 360.0f);
        boss.setXRot(0.0f);''')
sigil.write_text(s, encoding='utf-8')
print('Corregidos los seis errores detectados. Ejecuta gradle build para verificar.')
